##import some useful packages
import ROOT
import time
import numpy as np
import sys
import pandas as pd
import os
import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--tag", help = "tag", type=str, default = "test")
parser.add_argument("--combination", help = "combination boolean, combination =0", type=bool, default = 0)
args = parser.parse_args()

inputCCHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov16_ccYields/"
# inputCCHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/dec13_lep30_cc/"
# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov18_bdtYields/"
# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/dec2_bdtYields/"
# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/dec13_tthYieldsBDT/"
# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/dec16_ctagBDTYields/"

inputCCSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov23_ccSystematics/"
# inputBDTSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov23_bdtSystematics/"
# inputBDTBTagSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov18_bdtBTagSyst/"
# inputCCBTagSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov18_ccBTagSyst/"

inputCCJESUp = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov23_ccJESUp/"
inputCCJESDown = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov23_ccJESDown/"
# inputBDTJESUp = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov23_bdtJESUp/"
# inputBDTJESDown = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov23_bdtJESDown/"
inputBDTJESUp = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr27_jes_syst/"
inputBDTJESDown = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr27_jesDown_syst/"

# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan18_ctagBDT_normedCTagging/"
# inputBDTSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan19_ctag_syst/"
# inputBDTCtagSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/jan19_ctag_syst/"
# inputBDTLeptonSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/june23Syst_25/"

# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar27_smalltuhBDT/"
# inputBDTFakeEst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar27_smalltuhBDT/"
# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr7_fuckedupdata/"
# inputBDTFakeEst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr7_fuckedupdata/"
inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr8_fixedDataEG/"
inputBDTFakeEst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr8_fixedDataEG/"
# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/mar2_ctag_all/"
# inputBDTFakeEst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr27_fakeEst/"
inputBDTSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr26_syst/"
inputBDTCtagSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr26_syst/"
inputBDTLeptonSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/apr26_syst/"

# inputBDTHistos = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb22_jetpt30_SRylds/"
# inputBDTFakeEst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb22_jetpt30_SRylds/"
# inputBDTSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb16_jetpt30_systematics/newbins/"
# inputBDTCtagSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb16_jetpt30_systematics/newbins/"
# inputBDTLeptonSyst = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb16_jetpt30_systematics/newbins/"
# inputBDTJESUp = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb16_jetpt30_jesup/newbins/"
# inputBDTJESDown = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/feb16_jetpt30_jesdown/newbins/"

with open('./ccPDFScale.json') as ccScale_json: ccScale = json.load(ccScale_json)
with open('./bdtPDFScale.json') as bdtScale_json: bdtScale = json.load(bdtScale_json)
with open('./cc_fcnc_individual_uncs.json') as ccTh_json: ccThDict = json.load(ccTh_json)
with open('./bdt_fcnc_individual_uncs.json') as bdtTh_json: bdtThDict = json.load(bdtTh_json)
# with open('./bdt_fcnc_individual_uncs_separated.json') as bdtTh_json: bdtThDict = json.load(bdtTh_json)
with open('./cc_rare_individual_uncs.json') as ccThRare_json: ccThRareDict = json.load(ccThRare_json)
with open('./bdt_rare_individual_uncs.json') as bdtThRare_json: bdtThRareDict = json.load(bdtThRare_json)

#function to get CC SR titles
def getCCColumns(ccSRDict, numSRs):
    columns = []
    for key in ccSRDict:
        colTitle = "l"+str(ccSRDict[key]["nleps"])
        colTitle += "_j"+str(ccSRDict[key]["njets"])
        colTitle += "_b"+str(ccSRDict[key]["nbtags"])
        columns.append(colTitle)
    return columns

#function to get histogram from root file
def getObjFromFile(fname, hname):
    f = ROOT.TFile(fname)
    assert not f.IsZombie()
    f.cd()
    htmp = f.Get(hname)
    if not htmp:  return htmp
    ROOT.gDirectory.cd('PyROOT:/')
    res = htmp.Clone()
    f.Close()
    return res

with open('./ccSRbins.json') as ccbins_json: ccSRDict = json.load(ccbins_json)

years = [2016, 2017, 2018]
# years = [2016]
# signals = ["tuh"]
signals = ["tch", "tuh"]
procs = ["signal","rares","fakes_mc","flips_mc"]
mcProcs = ["signal_tch", "signal_tuh", "rares"]
ddProcs = ["fakes_mc","flips_mc"]

# systSources = ["LepSF","PU","Trigger","cferr1","cferr2","hf","hfstats1","hfstats2","lf","lfstats1","lfstats2"]
cc_systSources = ["LepSF","PU","Trigger","cferr1","cferr2","hf","hfstats1","hfstats2","lf","lfstats1","lfstats2"]
# cc_systSources = ["LepSF","PU","Trigger"]
bdt_systSources = ["EleSF","MuSF","EleSFsys","MuSFsys","PU","Trigger","lumi_uncorr","lumi_corr_161718","lumi_corr_1718","pdfShp16","pdfShp1718"]
# btagsystSources = ["cferr1","cferr2","hf","hfstats1","hfstats2","lf","lfstats1","lfstats2"]
bdt_ctagsystSources = [ "ctag_stat",
                    # "ctag_EleIDSF",
                    # "ctag_LHEScaleWeightmuF",
                    # "ctag_LHEScaleWeightmuR",
                    # "ctag_MuIDSF",
                    "ctag_PSWeightFSR",
                    "ctag_PSWeightISR",
                    # "ctag_PUWeight",
                    "ctag_XSecDYJets",
                    "ctag_XSecST",
                    "ctag_XSecWJets",
                    "ctag_XSecttbar",
                    "ctag_bFrag",
                    "ctag_jer",
                    # "ctag_jesTotal",
                    # "ctag_ValuesSystOnly",
                    #"ctag_TotalUnc"
                    ]#,"ctag_withMaxUncs"]
otherSyst = ["jes"]#,"pdfScale","renormScale"]

bdtSRs = ["bin_"+str(x) for x in range(20)]
ccSRs = getCCColumns(ccSRDict, 21)

##BDT CR JSON##
with open("./bdtRates.json") as bdtRates_json: bdtRates = json.load(bdtRates_json)
bdtCRstats = {}
for y in years:
    bdtCRstats[str(y)] = {}
    for s in signals:
        bdtCRstats[str(y)][s] = {}
        if "tch" in s: altSig = "hct"
        else: altSig = "hut"
        for p in ddProcs:
            bdtCRstats[str(y)][s][p] ={}
            # bdtFileName = inputBDTHistos + "data_" + str(y) + "_hists.root"
            if "fakes" in p:
                bdtFileName = inputBDTFakeEst + "data_" + str(y) + "_hists.root"
                sf = getObjFromFile(bdtFileName, "h_sf_bdtScore_"+altSig+"_data")
                mlsf = getObjFromFile(bdtFileName, "h_mlsf_bdtScore_"+altSig+"_data")
                hist = sf.Clone()
                hist.Add(mlsf)
            elif "flips" in p:
                bdtFileName = inputBDTHistos + "data_" + str(y) + "_hists.root"
                hist = getObjFromFile(bdtFileName, "h_os_bdtScore_"+altSig+"_data")
            iterator = 1
            for r in bdtSRs:
                bdtCRstats[str(y)][s][p][r] = {}
                bdtCRstats[str(y)][s][p][r]["yield"] = hist.GetBinContent(iterator)
                bdtCRstats[str(y)][s][p][r]["error"] = hist.GetBinError(iterator)
                bdtCRstats[str(y)][s][p][r]["syst"] = bdtRates[str(y)][s][r][p[:4]+"_syst"]
                iterator += 1

with open("./bdtCRStats.json", "w") as f_out: json.dump(bdtCRstats, f_out, indent=4)
print("finished BDT CR Stats")



##CC CR JSON##
with open("./ccRates.json") as ccRates_json: ccRates = json.load(ccRates_json)
ccCRstats = {}
for y in years:
    ccCRstats[str(y)] = {}
    for p in ddProcs:
        ccCRstats[str(y)][p] ={}
        ccFileName = inputCCHistos + "data_" + str(y) + "_hists.root"
        if "fakes" in p:
            sf = getObjFromFile(ccFileName, "h_sf_fakecr_data")
            mlsf = getObjFromFile(ccFileName, "h_mlsf_fakecr_data")
            hist = sf.Clone()
            hist.Add(mlsf)
        elif "flips" in p: hist = getObjFromFile(ccFileName, "h_os_flipcr_data")
        iterator = 1
        for r in ccSRs:
            ccCRstats[str(y)][p][r] = {}
            ccCRstats[str(y)][p][r]["yield"] = hist.GetBinContent(iterator)
            ccCRstats[str(y)][p][r]["error"] = hist.GetBinError(iterator)
            ccCRstats[str(y)][p][r]["syst"] = ccRates[str(y)][p][r]["syst"]
            iterator += 1

with open("./ccCRStats.json", "w") as f_out: json.dump(ccCRstats, f_out, indent=4)
print("finished CC CR Stats")



##BDT Systematics JSON##
bdtMCsyst = {}
for y in years:
    bdtMCsyst[str(y)] = {}
    for s in signals:
        bdtMCsyst[str(y)][s] = {}
        if "tch" in s: altSig = "hct"
        else: altSig = "hut"
        for p in mcProcs:
            if ("signal" in p) and (s not in p): continue
            bdtMCsyst[str(y)][s][p] = {}
            bdtFileName = inputBDTHistos + p + "_" + str(y) + "_hists.root"
            centralHist = getObjFromFile(bdtFileName, "h_br_bdtScore_" + altSig + "_" + p)
            print(bdtFileName, "h_br_bdtScore_" + altSig + "_" + p)
            ##Trigger,Lepton,PU,BTagging
            for t in bdt_systSources:
                # print(t)
                bdtMCsyst[str(y)][s][p][t] = {}
                if "lumi" in t:
                    if "uncorr" in t:
                        unc = 0
                        if y==2016: unc = 0.01
                        if y==2017: unc = 0.02
                        if y==2018: unc = 0.015
                        for r in bdtSRs:
                            bdtMCsyst[str(y)][s][p][t][r] = {}
                            bdtMCsyst[str(y)][s][p][t][r]["up"] = 1+unc
                            bdtMCsyst[str(y)][s][p][t][r]["down"] = 1-unc
                            # iterator += 1
                    else:
                        unc = 0
                        if "16" in t:
                            if y==2016: unc = 0.006
                            if y==2017: unc = 0.009
                            if y==2018: unc = 0.02
                        else:
                            if y==2017: unc = 0.006
                            if y==2018: unc = 0.002
                        for r in bdtSRs:
                            bdtMCsyst[str(y)][s][p][t][r] = {}
                            bdtMCsyst[str(y)][s][p][t][r]["up"] = 1+unc
                            bdtMCsyst[str(y)][s][p][t][r]["down"] = 1-unc
                            # iterator += 1
                elif "pdfShp" in t:
                    iterator = 1
                    for r in bdtSRs:
                        if (("signal" in p) and (s not in p)): continue 
                        bdtMCsyst[str(y)][s][p][t][r] = {}
                        bdtMCsyst[str(y)][s][p][t][r]["up"] = bdtScale[s][p]["bin_"+str(iterator-1)]["pdf_up"]
                        bdtMCsyst[str(y)][s][p][t][r]["down"] = bdtScale[s][p]["bin_"+str(iterator-1)]["pdf_down"]
                        iterator += 1
                else:
                    if "MuSF" in t: bdtSystFileName = inputBDTLeptonSyst + p + "_" + str(y) + "_hists.root"
                    elif "EleSF" in t: bdtSystFileName = inputBDTLeptonSyst + p + "_" + str(y) + "_hists.root"
                    else: bdtSystFileName = inputBDTSyst + p + "_" + str(y) + "_hists.root"
                    # print(bdtSystFileName)
                    # print("h_"+t+"_up_bdtScore_syst_"+ altSig + "_" +p)
                    if "SFsys" in t:
                        for r in bdtSRs:
                            bdtMCsyst[str(y)][s][p][t][r] = {}
                            bdtMCsyst[str(y)][s][p][t][r]["up"] = 1.02
                            bdtMCsyst[str(y)][s][p][t][r]["down"] = 0.98
                            iterator += 1
                    else:
                        upHist = getObjFromFile(bdtSystFileName, "h_"+t+"_up_bdtScore_syst_"+ altSig + "_" +p)
                        downHist = getObjFromFile(bdtSystFileName, "h_"+t+"_down_bdtScore_syst_"+ altSig + "_" +p)
                        print(bdtSystFileName)
                        print("h_"+t+"_up_bdtScore_syst_"+ altSig + "_" +p)
                        print("h_"+t+"_down_bdtScore_syst_"+ altSig + "_" +p)

                        upHist.Divide(centralHist)
                        downHist.Divide(centralHist)
                        iterator = 1
                        for r in bdtSRs:
                            bdtMCsyst[str(y)][s][p][t][r] = {}
                            # if "MuSF" in t or "EleSF" in t:
                            #     bdtMCsyst[str(y)][s][p][t][r]["up"] = upHist.GetBinContent(iterator)+0.05
                            #     bdtMCsyst[str(y)][s][p][t][r]["down"] = downHist.GetBinContent(iterator)-0.05
                            # else:
                            bdtMCsyst[str(y)][s][p][t][r]["up"] = upHist.GetBinContent(iterator)
                            bdtMCsyst[str(y)][s][p][t][r]["down"] = downHist.GetBinContent(iterator)
                            iterator += 1
            ##CTagging
            for t in bdt_ctagsystSources:
                # print(t)
                bdtMCsyst[str(y)][s][p][t] = {}
                bdtSystFileName = inputBDTCtagSyst + p + "_" + str(y) + "_hists.root"
                upHist = getObjFromFile(bdtSystFileName, "h_"+t+"_up_bdtScore_syst_"+ altSig + "_" +p)
                downHist = getObjFromFile(bdtSystFileName, "h_"+t+"_down_bdtScore_syst_"+ altSig + "_" +p)
                # print(bdtSystFileName)
                # print("h_"+t+"_up_bdtScore_syst_"+ altSig + "_" +p)
                # print("h_"+t+"_down_bdtScore_syst_"+ altSig + "_" +p)
                upHist.Divide(centralHist)
                downHist.Divide(centralHist)
                iterator = 1
                for r in bdtSRs:
                    bdtMCsyst[str(y)][s][p][t][r] = {}
                    bdtMCsyst[str(y)][s][p][t][r]["up"] = upHist.GetBinContent(iterator)
                    bdtMCsyst[str(y)][s][p][t][r]["down"] = downHist.GetBinContent(iterator)
                    iterator += 1
            ###BTAGGING
            ## bdtMCsyst[str(y)][s][p] ={}
            #bdtFileName = inputBDTSyst + p + "_" + str(y) + "_hists.root"
            #centralHist = getObjFromFile(bdtFileName, "h_btag_central_bdtScore_syst_" + altSig + str(y) + "_" + p)
            #for b in btagsystSources:
            #    bdtMCsyst[str(y)][s][p][b] ={}
            #    upHist = getObjFromFile(bdtFileName, "h_" + b + "_up_bdtScore_syst_" + altSig + str(y) + "_" + p)
            #    downHist = getObjFromFile(bdtFileName, "h_" + b + "_down_bdtScore_syst_" + altSig + str(y) + "_" + p)
            #    upHist.Divide(centralHist)
            #    downHist.Divide(centralHist)
            #    iterator = 1
            #    for r in bdtSRs:
            #        bdtMCsyst[str(y)][s][p][b][r] = {}
            #        bdtMCsyst[str(y)][s][p][b][r]["up"] = upHist.GetBinContent(iterator)
            #        bdtMCsyst[str(y)][s][p][b][r]["down"] = downHist.GetBinContent(iterator)
            #        iterator += 1
            ##JES
            bdtFileName = inputBDTHistos + p + "_" + str(y) + "_hists.root"
            centralHist = getObjFromFile(bdtFileName, "h_br_bdtScore_" + altSig + "_" + p)
            # print(bdtFileName)
            # print("h_br_bdtScore_" + altSig + "_" + p)
            bdtFileNameUp = inputBDTJESUp + p + "_" + str(y) + "_hists.root"
            upHist = getObjFromFile(bdtFileNameUp, "h_br_bdtScore_" + altSig + "_" + p)
            # print(bdtFileNameUp)
            # print("h_br_bdtScore_" + altSig + "_" + p)
            upHist.Divide(centralHist)
            bdtFileNameDown = inputBDTJESDown + p + "_" + str(y) + "_hists.root"
            downHist = getObjFromFile(bdtFileNameDown, "h_br_bdtScore_" + altSig + "_" + p)
            downHist.Divide(centralHist)
            bdtMCsyst[str(y)][s][p]["jes"] = {}
            iterator = 1
            for r in bdtSRs:
                bdtMCsyst[str(y)][s][p]["jes"][r] = {}
                bdtMCsyst[str(y)][s][p]["jes"][r]["up"] = upHist.GetBinContent(iterator)
                bdtMCsyst[str(y)][s][p]["jes"][r]["down"] = downHist.GetBinContent(iterator)
                iterator += 1
            ##PDF,SCALE
            bdtMCsyst[str(y)][s][p]["pdfShp"] = {}
            iterator = 1
            # for r in bdtSRs:
            #     if (("signal" in p) and (s not in p)): continue 
            #     bdtMCsyst[str(y)][s][p]["pdfShp"][r] = {}
            #     bdtMCsyst[str(y)][s][p]["pdfShp"][r]["up"] = bdtScale[s][p]["bin_"+str(iterator-1)]["pdf_up"]
            #     bdtMCsyst[str(y)][s][p]["pdfShp"][r]["down"] = bdtScale[s][p]["bin_"+str(iterator-1)]["pdf_down"]
            #     iterator += 1
            bdtMCsyst[str(y)][s][p][p[:3]+"ScShp"] = {}
            iterator = 1
            for r in bdtSRs:
                if (("signal" in p) and (s not in p)): continue 
                bdtMCsyst[str(y)][s][p][p[:3]+"ScShp"][r] = {}
                if(bdtScale[s][p]["bin_"+str(iterator-1)]["scale"] > 1):
                    bdtMCsyst[str(y)][s][p][p[:3]+"ScShp"][r]["up"] = bdtScale[s][p]["bin_"+str(iterator-1)]["scale"]
                    bdtMCsyst[str(y)][s][p][p[:3]+"ScShp"][r]["down"] = 2-bdtScale[s][p]["bin_"+str(iterator-1)]["scale"]
                else:
                    bdtMCsyst[str(y)][s][p][p[:3]+"ScShp"][r]["down"] = bdtScale[s][p]["bin_"+str(iterator-1)]["scale"]
                    bdtMCsyst[str(y)][s][p][p[:3]+"ScShp"][r]["up"] = 2-bdtScale[s][p]["bin_"+str(iterator-1)]["scale"]
                iterator += 1

            if args.combination:
                if "rare" in p:
                    bdtMCsyst[str(y)][s][p][p[:3]+"Th"] = {}
                else:
                    bdtMCsyst[str(y)][s][p][p[:3]+"Th_tt"] = {}
                    bdtMCsyst[str(y)][s][p][p[:3]+"Th_st"] = {}
                for r in bdtSRs:
                    if ("rare" in p):
                        fill_up = bdtThRareDict[str(y)][s][r]["up"]
                        fill_down = bdtThRareDict[str(y)][s][r]["down"]
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th"][r] = {}
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th"][r]["up"] = fill_up
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th"][r]["down"] = fill_down
                    else:
                        fill_up_tt = bdtThDict[str(y)][s][r]["tt"]["up"]
                        fill_down_tt = bdtThDict[str(y)][s][r]["tt"]["down"]
                        fill_up_st = bdtThDict[str(y)][s][r]["st"]["up"]
                        fill_down_st = bdtThDict[str(y)][s][r]["st"]["down"]
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th_tt"][r] = {}
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th_tt"][r]["up"] = fill_up_tt
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th_tt"][r]["down"] = fill_down_tt
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th_st"][r] = {}
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th_st"][r]["up"] = fill_up_st
                        bdtMCsyst[str(y)][s][p][p[:3]+"Th_st"][r]["down"] = fill_down_st
            else:
                bdtMCsyst[str(y)][s][p][p[:3]+"Th"] = {}
                for r in bdtSRs:
                    if ("rare" in p):
                        fill_up = bdtThRareDict[str(y)][s][r]["up"]
                        fill_down = bdtThRareDict[str(y)][s][r]["down"]
                    else:
                        fill_up = bdtThDict[str(y)][s][r]["up"]
                        fill_down = bdtThDict[str(y)][s][r]["down"]
                    bdtMCsyst[str(y)][s][p][p[:3]+"Th"][r] = {}
                    bdtMCsyst[str(y)][s][p][p[:3]+"Th"][r]["up"] = fill_up
                    bdtMCsyst[str(y)][s][p][p[:3]+"Th"][r]["down"] = fill_down

with open("./bdtMCsyst.json", "w") as f_out: json.dump(bdtMCsyst, f_out, indent=4)
print("finished BDT MC syst")



##CC Systematics JSON##
ccMCsyst = {}
for y in years:
    ccMCsyst[str(y)] = {}
    for p in mcProcs:
        ccMCsyst[str(y)][p] ={}
        ccFileName = inputCCHistos + p + "_" + str(y) + "_hists.root"
        centralHist = getObjFromFile(ccFileName, "h_br_sr_"+p)
        ##Trigger,Lepton,PU
        for s in cc_systSources:
            ccMCsyst[str(y)][p][s] = {}
            ccSystFileName = inputCCSyst + p + "_" + str(y) + "_hists.root"
            upHist = getObjFromFile(ccSystFileName, "h_"+s+"_up_sr_syst_"+p)
            downHist = getObjFromFile(ccSystFileName, "h_"+s+"_down_sr_syst_"+p)
            upHist.Divide(centralHist)
            downHist.Divide(centralHist)
            iterator = 1
            for r in ccSRs:
                ccMCsyst[str(y)][p][s][r] = {}
                ccMCsyst[str(y)][p][s][r]["up"] = upHist.GetBinContent(iterator)
                ccMCsyst[str(y)][p][s][r]["down"] = downHist.GetBinContent(iterator)
                iterator += 1
        # ##BTagging
        # # ccMCsyst[str(y)][p]["bTag"] = {}
        # ccSystFileName = inputCCSyst + p + "_" + str(y) + "_hists.root"
        # centralHist = getObjFromFile(ccSystFileName, "h_btag_central_sr_syst_"+p)        
        # for b in btagsystSources:
        #    ccMCsyst[str(y)][p][b] ={}
        #    upHist = getObjFromFile(ccSystFileName, "h_" + b + "_up_sr_syst_" + p)
        #    downHist = getObjFromFile(ccSystFileName, "h_" + b + "_down_sr_syst_" + p)
        #    upHist.Divide(centralHist)
        #    downHist.Divide(centralHist)
        #    iterator = 1
        #    for r in ccSRs:
        #        ccMCsyst[str(y)][p][b][r] = {}
        #        ccMCsyst[str(y)][p][b][r]["up"] = upHist.GetBinContent(iterator)
        #        ccMCsyst[str(y)][p][b][r]["down"] = downHist.GetBinContent(iterator)
        #        iterator += 1
        ##JES
        ccFileName = inputCCHistos + p + "_" + str(y) + "_hists.root"
        centralHist = getObjFromFile(ccFileName, "h_br_sr_" + p)
        ccFileNameUp = inputCCJESUp + p + "_" + str(y) + "_hists.root"
        upHist = getObjFromFile(ccFileNameUp, "h_br_sr_syst_" + p)
        upHist.Divide(centralHist)
        ccFileNameDown = inputCCJESDown + p + "_" + str(y) + "_hists.root"
        downHist = getObjFromFile(ccFileNameDown, "h_br_sr_syst_" + p)
        downHist.Divide(centralHist)
        ccMCsyst[str(y)][p]["jes"] = {}
        iterator = 1
        for r in ccSRs:
            ccMCsyst[str(y)][p]["jes"][r] = {}
            ccMCsyst[str(y)][p]["jes"][r]["up"] = upHist.GetBinContent(iterator)
            ccMCsyst[str(y)][p]["jes"][r]["down"] = downHist.GetBinContent(iterator)
            iterator += 1

        ##PDF,SCALE
        ccMCsyst[str(y)][p]["pdfShp"] = {}
        iterator = 1
        for r in ccSRs:
            ccMCsyst[str(y)][p]["pdfShp"][r] = {}
            ccMCsyst[str(y)][p]["pdfShp"][r]["up"] = ccScale[p][r]["pdf_up"]
            ccMCsyst[str(y)][p]["pdfShp"][r]["down"] = ccScale[p][r]["pdf_down"]
            iterator += 1

        ccMCsyst[str(y)][p][p[:3]+"ScShp"] = {}
        iterator = 1
        for r in ccSRs:
            # if (("signal" in p) and (s not in p)): continue 
            ccMCsyst[str(y)][p][p[:3]+"ScShp"][r] = {}
            ccMCsyst[str(y)][p][p[:3]+"ScShp"][r]["up"] = ccScale[p][r]["scale"]
            if(ccScale[p][r]["scale"] > 1):
                ccMCsyst[str(y)][p][p[:3]+"ScShp"][r]["down"] = 2-ccScale[p][r]["scale"]
            else:
                ccMCsyst[str(y)][p][p[:3]+"ScShp"][r]["down"] = 1+(1-ccScale[p][r]["scale"])
            iterator += 1

        ccMCsyst[str(y)][p][p[:3]+"Th"] = {}
        for r in ccSRs:
            if ("rare" in p): 
                for s in signals:
                    fill_up = ccThRareDict[str(y)][r]["up"]
                    fill_down = ccThRareDict[str(y)][r]["down"]
                    ccMCsyst[str(y)][p][p[:3]+"Th"][r] = {}
                    ccMCsyst[str(y)][p][p[:3]+"Th"][r]["up"] = fill_up
                    ccMCsyst[str(y)][p][p[:3]+"Th"][r]["down"] = fill_down
            else:
                fill_up = ccThDict[str(y)][p[-3:]][r]["up"]
                fill_down = ccThDict[str(y)][p[-3:]][r]["down"]
                ccMCsyst[str(y)][p][p[:3]+"Th"][r] = {}
                ccMCsyst[str(y)][p][p[:3]+"Th"][r]["up"] = fill_up
                ccMCsyst[str(y)][p][p[:3]+"Th"][r]["down"] = fill_down
with open("./ccMCsyst.json", "w") as f_out: json.dump(ccMCsyst, f_out, indent=4)
print("finished CC MC syst")

