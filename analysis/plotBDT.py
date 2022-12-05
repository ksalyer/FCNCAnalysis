import numpy as np

import uproot3
import matplotlib.pyplot as plt
import mplhep as hep
plt.style.use(hep.style.CMS)

from yahist import Hist1D, Hist2D

print("imported libraries")

# f_in = uproot3.open('/home/users/ksalyer/FranksFCNC/ana/analysis/outputs/v6BabyPlots/fakes_mc_2018_hists.root')

# path = '/home/users/ksalyer/FranksFCNC/ana/analysis/outputs/oct27_bdtScore/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/dec2_bdtYields/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan26_btagBDT_backgroundEstimate/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan18_ctagBDT_normedCTagging/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr16_ctag_backgroundestimates/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr19_ctag_mlonZ/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/may3_ctag_data_mc/'
path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov14_kinematics/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar2_ctag_all/'
# path_fakes   = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr27_fakeEst/"
# path_flips   = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr16_ctag_backgroundestimates/"
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar3_ctag_mlonz/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar3_ctag_fakeVal/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar3_ctag_rarebackgrounds/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan12_ogBDT/'
# path = '/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan03_ctagSFs/'
# path = '/home/users/ksalyer/FranksFCNC/ana/analysis/outputs/oct28_BDTInputs/'
# sigpath = '/home/users/ksalyer/FranksFCNC/ana/analysis/outputs/aug09_lead25_MET50_jet30_newTriggers_tt2or1l/'

regions =   [ #"mr",
             # "os",
             # "sf",
             # "df",
             # "mlsf",
             # "mldf",
             # "ss",
             # "ml",
             # "mlonz"
             "br",
             # "vrcr_fake",
             #"vrsr_ss",
             #"vrsr_ml",
             #"vrcr_sf",
             #"vrcr_df",
             #"vrcr_mlsf",
             #"vrcr_mldf",
             #"vrcr_flip",
             #"vrsr_flip"
            ]
variables = [   ["bdtScore_hct", 1, r'$HCT\ BDT\ score$'],
                ["bdtScore_hut", 1, r'$HUT\ BDT\ score$'],
                # ["bdtScoreOnZ_hct", 1, r'$HCT\ BDT\ score$'],
                # ["bdtScoreOnZ_hut", 1, r'$HUT\ BDT\ score$'],
                # ["fakeVal_bdtScore_hct", 1, r'$HCT\ BDT\ score$'],
                # ["fakeVal_bdtScore_hut", 1, r'$HUT\ BDT\ score$'],
                # ["bdtScore_evenBins_hct", 1, r'$HCT\ BDT\ score$'],
                # ["bdtScore_evenBins_hut", 1, r'$HUT\ BDT\ score$'],

                # #onZ
                # ["njOnZ", 1, r'$njets$'],
                # ["nbjOnZ", 1, r'$N_{b-jets}$'],
                # ["mOnZ", 1, r'$met$'],
                # ["zll", 1, r'$mll$'],
                # ["ljcscore", 1, r'$lead jet c score$'],
                # ["tjcscore", 1, r'$sublead jet c score$'],
                # ["thirdjcscore", 1, r'$subsublead jet c score$'],
                
                # #jets
                ["njets", 1, r'$N_{jets}$'],
                ["nbjets", 1, r'$N_{b-jets}$'],
                ["fwjpt", 1, r'$Most Forward Jet p_{T}$'],
                
                ["ljpt", 5, r'$p_T\ (lead.\ jet)\ (GeV)$'],
                ["ljbscore", 1, r'$lead.\ jet\ b-score$'],
                ["ljcscore", 1, r'$lead.\ jet\ c-score$'],
                
                ["tjpt", 5, r'$p_T\ (sublead.\ jet)\ (GeV)$'],
                ["tjbscore", 1, r'$sublead.\ jet\ b-score$'],
                ["tjcscore", 1, r'$sublead.\ jet\ c-score$'],
                
                ["thirdjpt", 5, r'$p_T\ (subsublead.\ jet)\ (GeV)$'],
                ["thirdjbscore", 1, r'$subsublead.\ jet\ b-score$'],
                ["thirdjcscore", 1, r'$subsublead.\ jet\ c-score$'],

                ["lbpt", 5, r'$p_T\ (lead.\ b-tag)\ (GeV)$'],
                ["lbscore", 5, r'$lead.\ b-tag\ b-score$'],

                # # Leptons
                # ["neles", 1, r'$N_{electrons}$'],
                # ["mll", 1, r'$m_{lead.\ lep,\ sublead.\ lep}$'],

                # ["llpt", 5, r'$p_T\ (lead.\ lep.)\ (GeV)$'],
                # # ["lleta", 1, r'$\eta\ (lead.\ lep.)$'],
                # ["lldxy", 4, r'$dxy\ (lead.\ lep.)$'],
                # ["lldz", 4, r'$dz\ (lead.\ lep.)$'],

                # ["ltpt", 5, r'$p_T\ (sublead.\ lep.)\ (GeV)$'],
                # # ["lteta", 4, r'$\eta\ (sublead.\ lep.)$'],
                # ["ltdxy", 4, r'$dxy\ (sublead.\ lep.)$'],
                # ["ltdz", 4, r'$dz\ (sublead.\ lep.)$'],

                # ["thirdlpt", 5, r'$p_T\ (subsublead.\ lep.)\ (GeV)$'],
                # # ["thirdleta", 4, r'$\eta\ (subsublead.\ lep.)$'],
                # ["thirdldxy", 4, r'$dxy\ (subsublead.\ lep.)$'],
                # ["thirdldz", 4, r'$dz\ (subsublead.\ lep.)$'],

                # #Event kinematics
                # ['met', 1, r'$MET\ (GeV)$'],
                # ['ht', 1, r'$HT\ (GeV)$'],
                # ['mt_ll_met', 1, r'$m_{T}\ (lead.\ lep,\ MET)\ (GeV)$'],
                # ['mt_tl_met', 1, r'$m_{T}\ (sublead.\ lep,\ MET)\ (GeV)$'],
                # ['mt_thirdl_met', 1, r'$m_{T}\ (subsublead.\ lep,\ MET)\ (GeV)$'],
            ]

# years = ["2016","2017","2018"]
years = ["2016","2017","2018","run2"]
# years = ["2016"]
blind = False
tuh_comb_systErrors = [615.1665225299698,229.3378743634561,153.31590751454064,126.47454331366515,100.17508163074972,79.31856523263973,67.05120343632984,60.816837025990196,49.39348645304188,46.25768369645387,42.89094924729396,37.2297690783601,32.89658317458452,30.219155596438103,29.681932828956924,21.638294897172862,18.516797909000495,21.5654660490506,13.503299002646026,9.133055915397582]
tch_comb_systErrors = [739.0621035530985,268.5313370780789,160.65522682872142,125.52094395482109,99.14397338941974,75.67594705360425,66.09131976443076,68.37490871728964,59.15939710900227,50.70247241999761,41.69109205390391,38.09224179360711,40.12931895985449,35.77924880520944,25.797026606756546,26.99706729048354,21.217829833856236,19.708382395139896,17.068916125023403,12.995443217544002]

print("got all initialization settings")

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

def change_uncertainty(hist, ax, newErrors, ratio=False):
    opts = {'step': 'post', 'label': 'Uncertainty', 'hatch': '///',
                    'facecolor': 'none', 'edgecolor': (0, 0, 0, .5), 'linewidth': 0, 'zorder':10.}
    # error = np.sqrt(hist.errors**2+(offset1*hist.counts)**2+(offset2*hist.counts)**2)
    
    if ratio:
        down = np.nan_to_num(np.ones(len(hist.counts)) - newErrors/hist.counts)
        up = np.nan_to_num(np.ones(len(hist.counts)) + newErrors/hist.counts)
    else:
        down = hist.counts-newErrors
        up = hist.counts+newErrors
    ax.fill_between(x=hist.edges, y1=np.r_[down, down[-1]], y2=np.r_[up, up[-1]], **opts)

print("defined functions")

for y in years:
    for r in regions:
        for var in variables:
            v = var[0]
            # if "bdtScore_h" in v: v+=y
            rebinVal = var[1]
            vname = var[2]
            histName = 'h_'+r+'_'+v+'_'+y
            print (histName)
            if r == 'os':
                hists = {
                    'fakes': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_'+r+'_'+v+'_fakes_mc'],
                    'top': uproot3.open(path+'top_'+y+'_hists.root')['h_'+r+'_'+v+'_top'],
                    'dy': uproot3.open(path+'dy_'+y+'_hists.root')['h_'+r+'_'+v+'_dy'],
                    'rares': uproot3.open(path+'os_rares_'+y+'_hists.root')['h_'+r+'_'+v+'_os_rares'],
                    'data': uproot3.open(path+'data_'+y+'_hists.root')['h_'+r+'_'+v+'_data'],
                    'tch': uproot3.open(path+'signal_tch_'+y+'_hists.root')['h_'+r+'_'+v+'_signal_tch'],
                    'tuh': uproot3.open(path+'signal_tuh_'+y+'_hists.root')['h_'+r+'_'+v+'_signal_tuh'],
                }
            elif r =='br':
                hists = {
                    'fakes': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_'+r+'_'+v+'_fakes_mc'],
                    'flips': uproot3.open(path+'flips_mc_'+y+'_hists.root')['h_'+r+'_'+v+'_flips_mc'],
                    # 'sf': uproot3.open(path_fakes+'data_'+y+'_hists.root')['h_sfest_'+v+'_data'],
                    # 'mlsf': uproot3.open(path_fakes+'data_'+y+'_hists.root')['h_mlsfest_'+v+'_data'],
                    # 'df': uproot3.open(path_fakes+'data_'+y+'_hists.root')['h_dfest_'+v+'_data'],
                    # 'mldf': uproot3.open(path_fakes+'data_'+y+'_hists.root')['h_mldfest_'+v+'_data'],
                    # 'sfpp':  uproot3.open(path+'rares_'+y+'_hists.root')['h_sfppest_'+v+'_rares'],
                    # 'mlsfppp':  uproot3.open(path+'rares_'+y+'_hists.root')['h_mlsfpppest_'+v+'_rares'],
                    # 'flips': uproot3.open(path+'data_'+y+'_hists.root')['h_osest_'+v+'_data'],
                    'rares': uproot3.open(path+'rares_'+y+'_hists.root')['h_'+r+'_'+v+'_rares'],
                    'data': uproot3.open(path+'data_'+y+'_hists.root')['h_'+r+'_'+v+'_data'],
                    'tch': uproot3.open(path+'signal_tch_'+y+'_hists.root')['h_'+r+'_'+v+'_signal_tch'],
                    'tuh': uproot3.open(path+'signal_tuh_'+y+'_hists.root')['h_'+r+'_'+v+'_signal_tuh'],

                    # 'multiboson': uproot3.open(path+'multiboson_'+y+'_hists.root')['h_'+r+'_'+v+'_multiboson'],
                    # 'ttw': uproot3.open(path+'ttw_'+y+'_hists.root')['h_'+r+'_'+v+'_ttw'],
                    # 'ttx': uproot3.open(path+'ttx_'+y+'_hists.root')['h_'+r+'_'+v+'_ttx'],
                    # 'ttvv': uproot3.open(path+'ttvv_'+y+'_hists.root')['h_'+r+'_'+v+'_ttvv'],
                    # 'xg': uproot3.open(path+'xg_'+y+'_hists.root')['h_'+r+'_'+v+'_xg'],
                    # 'smallRares': uproot3.open(path+'smallRares_'+y+'_hists.root')['h_'+r+'_'+v+'_smallRares']
                }
            elif r == 'vrcr_fake':
                hists = {
                    'estimate': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_vrcrest_fake_'+v+'_fakes_mc'],
                    'signal': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_vrsr_fake_'+v+'_fakes_mc'],
                }
            else:
                hists = {
                    'fakes': uproot3.open(path+'fakes_mc_'+y+'_hists.root')['h_'+r+'_'+v+'_fakes_mc'],
                    # 'flips': uproot3.open(path+'flips_mc_'+y+'_hists.root')['h_'+r+'_'+v+'_flips_mc'],
                    # 'fakes': uproot3.open(path+'data_'+y+'_hists.root')['h_mlsfest_'+v+'_data'],
                    # 'flips': uproot3.open(path+'data_'+y+'_hists.root')['h_osest_'+v+'_data'],
                    # 'rares': uproot3.open(path+'rares_'+y+'_hists.root')['h_'+r+'_'+v+'_rares'],
                    'rares': uproot3.open(path+'nonleadingrares_'+y+'_hists.root')['h_'+r+'_'+v+'_nonleadingrares'],
                    'ttw': uproot3.open(path+'ttw_'+y+'_hists.root')['h_'+r+'_'+v+'_ttw'],
                    'ttz': uproot3.open(path+'ttz_'+y+'_hists.root')['h_'+r+'_'+v+'_ttz'],
                    'tzq': uproot3.open(path+'tzq_'+y+'_hists.root')['h_'+r+'_'+v+'_tzq'],
                    'wz': uproot3.open(path+'wz_'+y+'_hists.root')['h_'+r+'_'+v+'_wz'],
                    'zz': uproot3.open(path+'zz_'+y+'_hists.root')['h_'+r+'_'+v+'_zz'],
                    'data': uproot3.open(path+'data_'+y+'_hists.root')['h_'+r+'_'+v+'_data'],
                    'tch': uproot3.open(path+'signal_tch_'+y+'_hists.root')['h_'+r+'_'+v+'_signal_tch'],
                    'tuh': uproot3.open(path+'signal_tuh_'+y+'_hists.root')['h_'+r+'_'+v+'_signal_tuh'],
                }

            if 'njets' in v:
                my_histos = { x:get_yahist(hists[x], rebin=rebinVal, overflow=True, newEdges=[float('-inf'),-0.5,0.5,1.5,2.5,3.5,4.5,float('inf')]) for x in hists.keys() }
            elif 'nbjets' in v:
                my_histos = { x:get_yahist(hists[x], rebin=rebinVal, overflow=True, newEdges=[float('-inf'),-0.5,0.5,1.5,2.5,float('inf')]) for x in hists.keys() }
            else:
                my_histos = { x:get_yahist(hists[x], rebin=rebinVal, overflow=True) for x in hists.keys() }

            # my_histos['top'] = my_histos['top']*2
            # my_histos['dy'] = my_histos['dy']*2
            # flipDataSF = (sum(my_histos['data'].counts)-sum(my_histos['top'].counts))/(sum(my_histos['data_est'].counts))
            # print(flipDataSF)
            # my_histos['data_est'] *= flipDataSF
            # my_histos['dy'] *= flipDataSF
            # if r == 'br':
            #     my_histos['fakes'] = my_histos['sf']+my_histos['mlsf']-my_histos['df']-my_histos['df']-my_histos['mldf']-my_histos['mldf']-my_histos['sfpp']-my_histos['mlsfppp']
            #     print('fakes', my_histos['fakes'].counts)
            #     print('flips', my_histos['flips'].counts)
            #     print('rares', my_histos['rares'].counts)


            if r == 'os':
                my_histos['fakes'].label = 'Nonprompt'
                my_histos['fakes'].color = '#FF595E'

                # my_histos['tw'].label = 'tW'
                # my_histos['tw'].color = '#FF595E'

                my_histos['top'].label = 'tt2l'
                my_histos['top'].color = '#FFCA3A'

                my_histos['dy'].label = 'Drell Yan'
                my_histos['dy'].color = '#08BDBD'

                my_histos['rares'].label = 'Other'
                my_histos['rares'].color = '#8AC926'

                keys = ['rares', 'fakes', 'dy', 'top']
                # keys = ['rares', 'dy', 'fakes']

            elif r == 'vrcr_fake':
                my_histos['estimate'].label = "Nonprompt Estimate"
                my_histos['estimate'].color = '#FF595E'

                keys = ['estimate']

            else: 

                my_histos['fakes'].label = 'Nonprompt'
                my_histos['fakes'].color = '#FF595E'

                my_histos['flips'].label = 'Charge flip'
                my_histos['flips'].color = '#FFCA3A'

                my_histos['rares'].label = 'Other'
                my_histos['rares'].color = '#8AC926'

                # my_histos['ttz'].label = 'ttZ'
                # my_histos['ttz'].color = '#8AC926'

                # my_histos['ttw'].label = 'ttW'
                # my_histos['ttw'].color = '#FFCA3A'

                # my_histos['tzq'].label = 'tZq'
                # my_histos['tzq'].color = '#FF99C9'

                # my_histos['wz'].label = 'WZ'
                # my_histos['wz'].color = '#08BDBD'

                # my_histos['zz'].label = 'ZZ'
                # my_histos['zz'].color = '#F96E46'

                # my_histos['rares'].label = 'OtherRares'
                # my_histos['rares'].color = '#6987C9'

                # my_histos['top'].label = 'tt/tw/ttg'
                # my_histos['top'].color = '#FF595E'

                # my_histos['dy'].label = 'DY'
                # my_histos['dy'].color = '#FFCA3A'

                # my_histos['wboson'].label = 'wjets/wg'
                # my_histos['wboson'].color = '#8AC926'

                # my_histos['smallRares'].label = 'Higgs'
                # my_histos['smallRares'].color = '#FF99C9'

                # my_histos['xg'].label = r'$X +\gamma$'
                # my_histos['xg'].color = '#6987C9'

                # my_histos['ttvv'].label = 'ttXX'
                # my_histos['ttvv'].color = '#8AC926'

                # # my_histos['triboson'].label = 'VVV'
                # # my_histos['triboson'].color = '#FF99C9'

                # my_histos['ttx'].label = 'ttX'
                # my_histos['ttx'].color = '#FFCA3A'

                # my_histos['ttw'].label = 'ttW'
                # my_histos['ttw'].color = '#08BDBD'

                # my_histos['multiboson'].label = 'VV/VVV'
                # my_histos['multiboson'].color = '#FF595E'

                keys = ['flips', 'rares', 'fakes']
                # keys = [ 'ttw','tzq','ttz','fakes','rares', 'zz','wz']
                # keys = ['smallRares','xg', 'ttvv','ttx', 'ttw','multiboson']
                # keys = ['wboson','dy','top']
                # keys = ['dy', 'xg', 'wboson','top']
                # keys = ['estimate']

            if r == 'vrcr_fake':
                signals = ['signal']
            else:
                signals = ['tch', 'tuh']

            total_mc = get_total(my_histos, keys)

            # mcDataSF = (sum(my_histos['data'].counts))/(sum(total_mc.counts))

            # for k in keys:
            #     my_histos[k] *= mcDataSF
            # total_mc = get_total(my_histos, keys)


            if not (blind and (r == 'ss' """or r == 'ml'""" or r == 'br')): 
                ratio = my_histos['data'].divide(total_mc, )
            #     # ratio_est = my_histos['data_est'].divide(total_mc, )
            #     # ratio_data = my_histos['data'].divide(my_histos['data_est'], )
            else:
                ratio_tch = my_histos['tch'].divide(total_mc, )
                ratio_tuh = my_histos['tuh'].divide(total_mc, )

            # ratio = my_histos['estimate'].divide(my_histos['signal'])

            # f, ax = plt.subplots()

            fig, (ax, rax) = plt.subplots(2,1,figsize=(10,10), gridspec_kw={"height_ratios": (3, 1), "hspace": 0.05}, sharex=True)
            # fig, ax = plt.subplots(1,1,figsize=(10,10))

            if y == "2016": luminosity = 35.9
            if y == "2017": luminosity = 41.5
            if y == "2018": luminosity = 59.71
            if y == "run2": luminosity = 137
            hep.cms.label(
                "Preliminary",
                data=True,
                #year=2018,
                lumi=luminosity,
                loc=0,
                ax=ax,
            )

            hep.histplot(
                [ my_histos[x].counts for x in keys ],
                my_histos['fakes'].edges,
                # my_histos['multiboson'].edges,
                # my_histos['estimate'].edges,
                w2=[ my_histos[x].errors for x in keys ],
                histtype="fill",
                stack=True,
                # label=['%s (%.0f)'%(my_histos[x].label, sum(my_histos[x].counts)) for x in keys],
                label=['%s'%(my_histos[x].label) for x in keys],
                color=[ my_histos[x].color for x in keys ],
                ax=ax)

            if not (blind and (r == 'ss' """or r == 'ml'""" or r == 'br')):
                hep.histplot(
                    my_histos['data'].counts,
                    my_histos['data'].edges,
                    yerr=my_histos['data'].errors,
                    histtype="errorbar",
                    stack=False,
                    # label='%s (%.0f)'%('Observation', sum(my_histos['data'].counts)),
                    label='%s'%('Observation'),
                    color='black',
                    ax=ax)

                # hep.histplot(
                #     my_histos['data_est'].counts,
                #     my_histos['data_est'].edges,
                #     yerr=my_histos['data_est'].errors,
                #     histtype="errorbar",
                #     stack=False,
                #     label='%s (%.0f)'%('Data (est)', sum(my_histos['data_est'].counts)),
                #     color='grey',
                #     ax=ax)

            hep.histplot(
                [my_histos['tch'].counts/100, my_histos['tuh'].counts/100],
                my_histos['tch'].edges,
                w2=[my_histos['tch'].errors/100, my_histos['tuh'].errors/100],
                histtype="step",
                stack=False,
                label=[r'$B(t\to Hc)=0.01$', r'$B(t\to Hu)=0.01$'],
                # color=['#525B76','#6A4C93'],
                color=['#525B76','#BC412B'],
                ax=ax)

            # hep.histplot(
            #     [my_histos['signal'].counts],
            #     my_histos['signal'].edges,
            #     w2=[my_histos['signal'].errors],
            #     histtype="step",
            #     stack=False,
            #     label=[r'$Validation SR$'],
            #     # color=['#525B76','#6A4C93'],
            #     color=['#525B76'],
            #     ax=ax)

            # hep.histplot(
            #     ratio.counts,
            #     ratio.edges,
            #     yerr=my_histos['estimate'].errors/my_histos['signal'].counts,
            #     histtype="errorbar",
            #     color='black',
            #     ax=rax)
            # # print(my_histos['estimate'].counts)
            # # print(my_histos['estimate'].errors)
            # # print(total_mc.errors)
            # # print(my_histos['signal'].errors)
            # # print(my_histos['estimate'].errors/my_histos['signal'].counts)

            if not (blind and (r == 'ss' """or r == 'ml'""" or r == 'br')):
                # print("making data plot")
                # print(ratio.counts)
                hep.histplot(
                    ratio.counts,
                    ratio.edges,
                    yerr=my_histos['data'].errors/total_mc.counts,
                    histtype="errorbar",
                    color='black',
                    ax=rax)

            #     # hep.histplot(
            #     #     ratio_est.counts,
            #     #     ratio_est.edges,
            #     #     yerr=my_histos['data_est'].errors/total_mc.counts,
            #     #     histtype="errorbar",
            #     #     color='grey',
            #     #     ax=rax)

            #     # hep.histplot(
            #     #     ratio_data.counts,
            #     #     ratio_data.edges,
            #     #     yerr=my_histos['data'].errors/my_histos['data_est'].counts,
            #     #     histtype="errorbar",
            #     #     color='black',
            #     #     ax=rax)
            # else:
            #     hep.histplot(
            #         [ratio_tch.counts/100, ratio_tuh.counts/100],
            #         ratio_tch.edges,
            #         w2=[ratio_tch.errors/100, ratio_tuh.errors/100],
            #         histtype="errorbar",
            #         color=['#525B76','#6A4C93'],
            #         ax=rax)


            rax.set_ylim(0,1.99)
            # rax.set_ylim(0.7,1.3)
            #rax.set_xlabel(r'$p_T\ (lead.\ lep.)\ (GeV)$')
            rax.set_xlabel(vname)
            # if not (blind and (r == 'ss' or r == 'ml' or r == 'br')): rax.set_ylabel(r'Data/Sim.')
            # if not (blind and (r == 'ss' """or r == 'ml'""" or r == 'br') or r == 'os'): rax.set_ylabel(r'Obs./Pred.')
            rax.set_ylabel(r'Obs./Pred.')
            # else: rax.set_ylabel(r'Sig./Back.')
            ax.set_ylabel(r'Events')
            ax.set_yscale('log')
            # ax.set_ylim(1,1e10)
            ax.set_ylim(0.1,1e9)
            # ax.set_xlabel(vname)
            # ax.set_yscale('linear')
            # ax.set_ylim(0.1, 10000)

            # add_uncertainty(total_mc, rax, ratio=True)#, offset1=0.3)
            # add_uncertainty(total_mc, ax)#, offset1=0.3)
            if y == "run2" and "hut" in v:
                change_uncertainty(total_mc, rax, tuh_comb_systErrors, ratio=True)#, offset1=0.3)
                change_uncertainty(total_mc, ax, tuh_comb_systErrors)#, offset1=0.3)
            elif y == "run2" and "hct" in v:
                change_uncertainty(total_mc, rax, tch_comb_systErrors, ratio=True)#, offset1=0.3)
                change_uncertainty(total_mc, ax, tch_comb_systErrors)#, offset1=0.3)
            else:
                add_uncertainty(total_mc, rax, ratio=True)#, offset1=0.3)
                add_uncertainty(total_mc, ax)#, offset1=0.3)


            ax.legend(ncol=2)

            #plt.show()

            fig.savefig('/home/users/ksalyer/public_html/FCNC_plots/nov14_kinematics/'+histName+'.png')
            fig.savefig('/home/users/ksalyer/public_html/FCNC_plots/nov14_kinematics/'+histName+'.pdf')
            #plt.close()
