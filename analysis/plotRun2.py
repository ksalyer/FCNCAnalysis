import numpy as np

import uproot3
import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.style.CMS)

from yahist import Hist1D, Hist2D

# f_in = uproot3.open('/home/users/ksalyer/FranksFCNC/ana/analysis/outputs/v6BabyPlots/fakes_mc_2018_hists.root')

path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan26_btagBDT_validationTests/'

variables = [   ["fakeVal_bdtScore_hct", 1, r'$HCT\ BDT\ score$'],
                ["fakeVal_bdtScore_hut", 1, r'$HUT\ BDT\ score$'],
            ]

years = ["2016","2017","2018"]
# years = ["2016"]
blind = True


def get_yahist(hist, rebin=1, overflow=True, newEdges=[]):
    counts = hist.allvalues
    edges = hist.alledges
    w2 = hist.allvariances
    if newEdges: 
        edges = newEdges
        sliceCounts = counts[len(edges)-2:]
        counts = counts[:len(edges)-1]
        np.append(counts,sum(sliceCounts))
        neww2 = w2[:len(edges)-1]
        np.append(neww2,sum(counts[len(edges)-2:]))
        w2 = neww2
    # print (edges, len(edges))
    # print(counts, len(counts))
    if overflow:
        counts[1] += counts[0]
        counts[-2] += counts[-1]
        w2[1] += w2[1]
        w2[-2] += w2[-1]
        counts = np.array(counts[1:-1])
        edges = np.array(edges[1:-1])
        w2 = np.array(w2[1:-1])

    
    tmp_hist = Hist1D.from_bincounts(counts, edges, np.sqrt(w2), )
    if rebin!=1: tmp_hist = tmp_hist.rebin(rebin)
    return tmp_hist

def get_total(histos, keys):
    tmp = Hist1D.from_bincounts(np.zeros(len(histos[keys[0]].counts)), histos[keys[0]].edges, )
    for key in keys:
        tmp += histos[key]
    
    return tmp

def add_uncertainty(hist, ax, ratio=False, offset1 = 0.0, offset2 = 0.0):
    opts = {'step': 'post', 'label': 'Uncertainty', 'hatch': '///',
                    'facecolor': 'none', 'edgecolor': (0, 0, 0, .5), 'linewidth': 0, 'zorder':10.}
    error = np.sqrt(hist.errors**2+(offset1*hist.counts)**2+(offset2*hist.counts)**2)
    
    if ratio:
        down = np.nan_to_num(np.ones(len(hist.counts)) - error/hist.counts)
        up = np.nan_to_num(np.ones(len(hist.counts)) + error/hist.counts)
    else:
        down = hist.counts-error
        up = hist.counts+error
    ax.fill_between(x=hist.edges, y1=np.r_[down, down[-1]], y2=np.r_[up, up[-1]], **opts)


for y in years:
    for var in variables:
        v = var[0]
        if "bdtScore_h" in v: v+=y
        rebinVal = var[1]
        vname = var[2]
        histName = 'h_closureTest_'+v+'_'+y
        print (histName)
        hists = {
            'vrcrest': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_vrcrest_fake_'+v+'_fakes_mc'],
            'vrsr': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_vrsr_fake_'+v+'_fakes_mc'],
        }

        my_histos = { x:get_yahist(hists[x], rebin=rebinVal, overflow=True) for x in hists.keys() }

        my_histos['vrcrest'].label = 'Nonprompt Estimate (tt)'
        my_histos['vrcrest'].color = '#FF595E'

        my_histos['vrsr'].label = 'Nonprompt in SR'
        my_histos['vrsr'].color = '#525B76'

        ratio = my_histos['vrcrest'].divide(my_histos['vrsr'])

        fig, (ax, rax) = plt.subplots(2,1,figsize=(10,10), gridspec_kw={"height_ratios": (3, 1), "hspace": 0.05}, sharex=True)

        if y == "2016": luminosity = 36.3
        if y == "2017": luminosity = 41.5
        if y == "2018": luminosity = 59.7

        hep.cms.label(
            "Preliminary",
            data=True,
            #year=2018,
            lumi=luminosity,
            loc=0,
            ax=ax,
        )

        hep.histplot(
            [ my_histos['vrcrest'].counts ],
            my_histos['vrcrest'].edges,
            w2=[ my_histos['vrcrest'].errors ],
            histtype="fill",
            stack=True,
            label=['%s'%(my_histos['vrcrest'].label)],
            color=[ my_histos['vrcrest'].color ],
            ax=ax)

        hep.histplot(
            [my_histos['vrsr'].counts],
            my_histos['vrsr'].edges,
            w2=[my_histos['vrsr'].errors],
            histtype="step",
            stack=False,
            label=['%s'%(my_histos['vrsr'].label)],
            color=[ my_histos['vrsr'].color ],
            ax=ax)

        hep.histplot(
            ratio.counts,
            ratio.edges,
            yerr=my_histos['vrcrest'].errors/my_histos['vrsr'].counts,
            histtype="errorbar",
            color='black',
            ax=rax)

        rax.set_ylim(0,1.99)
        rax.set_xlabel(vname)
        rax.set_ylabel(r'Estimate/Sim.Truth')
        ax.set_ylabel(r'Events')
        ax.set_yscale('log')
        ax.set_ylim(1,1e4)
        # ax.set_xlabel(vname)
        # ax.set_yscale('linear')
        # ax.set_ylim(0.1, 10000)

        add_uncertainty(my_histos['vrcrest'], rax, ratio=True, offset1 = 0.2)
        add_uncertainty(my_histos['vrcrest'], ax, ratio=False, offset1 = 0.2)

        ax.legend()
        # ax.legend(ncol=2)

        #plt.show()

        fig.savefig('/home/users/ksalyer/public_html/FCNC_plots/'+histName+'.png')
        fig.savefig('/home/users/ksalyer/public_html/FCNC_plots/'+histName+'.pdf')
        #plt.close()
