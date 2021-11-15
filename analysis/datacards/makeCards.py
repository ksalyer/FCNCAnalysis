##import some useful packages
import ROOT
import time
import numpy as np
import sys
import pandas as pd
import os
import json


## HARDCODED PATHS TO INPUT HISTOS ##
inFilePath = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov14_hists/"
#inFilePath = "/home/users/ksalyer/FCNCAnalysis/analysis/outputs/nov15_yields/"

##define functions
#function to get multiplicities for a given cc bin
def getCCSRBin(binIdx, hist, ccSRDict):
    yld = hist.GetBinContent(binIdx)
    err = hist.GetBinError(binIdx)
    nl = ccSRDict[str(binIdx)]["nleps"]
    nj = ccSRDict[str(binIdx)]["njets"]
    nb = ccSRDict[str(binIdx)]["nbtags"]
    srName = "l"+str(nl)+"_j"+str(nj)+"_b"+str(nb)
    return {"nleps":nl,
            "njets":nj,
            "nbtags":nb,
            "yield":yld,
            "error":err,
            "name":srName}

#function to make CC column titles
def getCCColumns(ccSRDict, numSRs):
    columns = []
    for key in ccSRDict:
        colTitle = "l"+str(ccSRDict[key]["nleps"])
        colTitle += "_j"+str(ccSRDict[key]["njets"])
        colTitle += "_b"+str(ccSRDict[key]["nbtags"])
        columns.append(colTitle)
    return columns

#function to make the SR stat row titles
def getSRStatRows(processes, numSRs):
    titles = []
    for p in processes:
        for i in range(numSRs):
            rowTitle = p[:3]
            rowTitle += "_stat_"
            rowTitle += str(i)
            while len(rowTitle) < 17: rowTitle += " "
            rowTitle += "lnN"
            titles.append(rowTitle)
    return titles

#function to make the CR stat and dd rate Syst row titles
def getCRStatRows(year, processes, SRs, CRDict):
    titles = []
    for p in processes:
        for i in range(len(SRs)): 
            if "flips" in p and CRDict[str(year)][p][SRs[i]]["yield"]==0: continue
            rowTitle = p[:2]
            rowTitle += "_st"
            rowTitle += str(i)
            rowTitle += "_"+str(y)[-2:]+" "
            rowTitle += str(CRDict[str(year)][p][SRs[i]]["yield"])
            while len(rowTitle) < 17: rowTitle += " "
            rowTitle += "gmN"
            titles.append(rowTitle)
        rowTitle = p[:4]
        rowTitle += "RateSyst_"
        rowTitle += str(y)[-2:]
        while len(rowTitle) < 17: rowTitle += " "
        rowTitle += "lnN"
        titles.append(rowTitle)
    return titles

#function to make the Syst row titles
def getSystRows(year, correlated, uncorrelated):
    titles = []
    for c in correlated:
        rowTitle = c
        while len(rowTitle)<17: rowTitle+=" "
        rowTitle += "lnN"
        titles.append(rowTitle)
    for u in uncorrelated:
        rowTitle = u
        rowTitle += "_" + str(year)[-2:]
        while len(rowTitle)<17: rowTitle+=" "
        rowTitle += "lnN"
        titles.append(rowTitle)
    return titles

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

##load useful jsons
with open('./ccSRbins.json') as ccbins_json: ccSRDict = json.load(ccbins_json)
with open('./ccCRStats.json') as ccCR_json: ccCRDict = json.load(ccCR_json)

##lists to loop
numCCSRs = 21
numBDTSRs = 20
years = [2016,2017,2018]
signals = ["tch","tuh"]
procs   = ["signal","rares","fakes_mc","flips_mc"]
mcProcs = ["signal","rares"]
ddProcs = ["fakes_mc","flips_mc"]
corrSyst = ["rarTh","sigTh","pdfShp","rarScShp","sigScShp","PU","lf","hf","cferr1","cferr2"]
uncorrSyst = ["jes","Trigger","LepSF","lfstats1","lfstats2","hfstats1","hfstats2"]

## main loop
for y in years:
    for s in signals:
        ## CUT AND COUNT COLUMNS, ROWS, AND DATAFRAME ##
        ccSRs = getCCColumns(ccSRDict, numCCSRs)
        ccDFCols = [b+"_"+p[:3] for b in ccSRs for p in procs]

        ccRows = []
        ccRows += getSRStatRows(mcProcs, numCCSRs)
        ccRows += getCRStatRows(y, ddProcs, ccSRs, ccCRDict)
        ccRows += getSystRows(y, corrSyst, uncorrSyst)

        cc_df = pd.DataFrame(columns = ccDFCols, index = ccRows)

        ## BDT COLUMNS, ROWS, AND DATAFRAME ##
        bdtSRs = ["bin_"+str(x) for x in range(20)]
        bdtDFCols = [b+"_"+p[:3] for b in bdtSRs for p in procs]

        bdtRows = []
        bdtRows += getSRStatRows(mcProcs, numBDTSRs)
        # bdtRows += getCRStatRows(y, ddProcs, ccSRs, ccCRDict)
        bdtRows += getSystRows(y, corrSyst, uncorrSyst)

        bdt_df = pd.DataFrame(columns = bdtDFCols, index = bdtRows)


        ## FILL MC ESTIMATES ##
        for p in mcProcs:
            if "signal" in p:
                fileName = inFilePath + p + "_" + s + "_" + str(y) + "_hists.root"
                srHist = getObjFromFile(fileName, "h_br_sr_signal_"+s)
            else:
                fileName = inFilePath + p + "_" + str(y) + "_hists.root"
                srHist = getObjFromFile(fileName, "h_br_sr_"+p)
            for i in range(1, numCCSRs+1):
                binDict = getCCSRBin(i, srHist, ccSRDict)
                colTitle = binDict["name"] + "_" + p[:3]
                rowTitle = p[:3] + "_stat_" + str(i-1)
                while len(rowTitle)<17: rowTitle += " "
                rowTitle += "lnN"
                fill = 1+round(binDict["error"]/binDict["yield"], 8)
                fill = str(fill)
                while len(fill) <20: fill += " "
                cc_df[colTitle][rowTitle] = fill


        ## FILL DATA DRIVEN ESTIMATES ##
        for p in ddProcs:
            fileName = inFilePath + "data_" + str(y) + "_hists.root" 
            
            # this is the correct name, but these histograms aren't made yet, so for the sake of testing this script,
            # I'm using the uncommented version
            # if "fakes" in p: 
            #     raresFile = inFilePath + "rares_" + str(y) + "_hists.root"

            #     sfHist = getObjFromFile(fileName, "h_sfest_fakecr_data")
            #     mlsfHist = getObjFromFile(fileName, "h_mlsfest_fakecr_data")
            #     dfHist = getObjFromFile(fileName, "h_dfest_fakecr_data")
            #     mldfHist = getObjFromFile(fileName, "h_mldfest_fakecr_data")
            #     sfppHist = getObjFromFile(raresFile, "h_sfppest_fakecr_rares")
            #     mlsfppHist = getObjFromFile(raresFile, "h_mlsfppest_fakecr_rares")

            #     srHist = sfHist.Clone()
            #     srHist.Add(mlsfHist)
            #     srHist.Add(dfHist, -2)
            #     srHist.Add(mldfHist, -2)
            #     srHist.Add(sfppHist, -1)
            #     srHist.Add(mlsfppHist, -1)
            # else: srHist = getObjFromFile(fileName, "h_osest_flipcr_data")
            if "fakes" in p: srHist = getObjFromFile(fileName, "h_sfest_sr_data")
            else: srHist = getObjFromFile(fileName, "h_osest_sr_data")

            for i in range(1, numCCSRs+1):
                binDict = getCCSRBin(i, srHist, ccSRDict)
                if "flip" in p and ccCRDict[str(y)][p][binDict["name"]]["yield"]==0: continue
                coltitle = binDict["name"] + "_" + p[:3]
                rowTitle = p[:2] + "_st" + str(i-1) + "_" + str(y)[-2:] + " "
                rowTitle += str(ccCRDict[str(y)][p][binDict["name"]]["yield"])
                while len(rowTitle)<17: rowTitle += " "
                rowTitle += "gmN"
                fill = round(binDict["yield"]/ccCRDict[str(y)][p][binDict["name"]]["yield"], 8)
                fill = str(fill)
                while len(fill)<20: fill += " "
                cc_df[colTitle][rowTitle] = fill
                rowTitle = p[:4] + "RateSyst_" + str(r)[-2:]
                while len(rowTitle)<17: rowTitle += " "
                fill = round(1+ (ccCRDict[str(y)][p][binDict["name"]]["syst"]/100), 8)
                fill = str(fill)
                while len(fill)<20: fill += " "
                cc_df[colTitle][rowTitle] = fill

        print(cc_df)




















# #hardcoded variables other users should customize
# with open('./outputs/aug31_systematics/fcnc_individual_uncs.json') as theory_json:
#     theory_unc = json.load(theory_json)
# with open('./outputs/aug31_systematics/scaleErrorOutput.txt') as theoryShapeTxt:
#     for line in theoryShapeTxt:
#         if "tch:\t" in line:
#             tchShapeUnc = line.split("\t")
#             del tchShapeUnc[0]
#             lastidx = len(tchShapeUnc)-1
#             lastele = tchShapeUnc[lastidx]
#             lastele = lastele[:-1]
#             tchShapeUnc[lastidx] = lastele
#         if "tuh:\t" in line:
#             tuhShapeUnc = line.split("\t")
#             del tuhShapeUnc[0]
#             lastidx = len(tuhShapeUnc)-1
#             lastele = tuhShapeUnc[lastidx]
#             lastele = lastele[:-1]
#             tuhShapeUnc[lastidx] = lastele
#         if "rares:\t" in line:
#             raresShapeUnc = line.split("\t")
#             del raresShapeUnc[0]
#             lastidx = len(raresShapeUnc)-1
#             lastele = raresShapeUnc[lastidx]
#             lastele = lastele[:-1]
#             raresShapeUnc[lastidx] = lastele
# with open('./outputs/aug31_systematics/pdfErrorOutput.txt') as pdfShapeTxt:
#     for line in pdfShapeTxt:
#         if "tch:\t" in line:
#             tchPDFShapeUnc = line.split("\t")
#             del tchPDFShapeUnc[0]
#             lastidx = len(tchPDFShapeUnc)-1
#             lastele = tchPDFShapeUnc[lastidx]
#             lastele = lastele[:-1]
#             tchPDFShapeUnc[lastidx] = lastele
#         if "tuh:\t" in line:
#             tuhPDFShapeUnc = line.split("\t")
#             del tuhPDFShapeUnc[0]
#             lastidx = len(tuhPDFShapeUnc)-1
#             lastele = tuhPDFShapeUnc[lastidx]
#             lastele = lastele[:-1]
#             tuhPDFShapeUnc[lastidx] = lastele
#         if "rares:\t" in line:
#             raresPDFShapeUnc = line.split("\t")
#             del raresPDFShapeUnc[0]
#             lastidx = len(raresPDFShapeUnc)-1
#             lastele = raresPDFShapeUnc[lastidx]
#             lastele = lastele[:-1]
#             raresPDFShapeUnc[lastidx] = lastele
# # print(tchPDFShapeUnc)
# # print(tuhPDFShapeUnc)
# outdir = "/home/users/ksalyer/FranksFCNC/ana/analysis/datacards/"
# indir = "test/"
# outdir = outdir+indir+"/oct13_changeInSigBR/"
# if not os.path.exists(outdir): os.makedirs(outdir)
# years = [2016, 2017, 2018]
# includeSignalInObs = False


# if not os.path.exists(outdir): os.makedirs(outdir)

# for y in years:

#     #now we have imported the data and manipulated it into the categories we want
#     #we will do the rest in a loop over signals
#     signals = ["signal_tuh","signal_tch"]
#     for s in signals:
#         if "tch" in s: signalSyst_df = tchSyst_df
#         else: signalSyst_df = tuhSyst_df
#         outfileName = "datacard_"
#         outfileName+=s
#         outfileName+="_"
#         outfileName+=str(y)
#         outfileName+=".txt"

#         #signal region bins
#         nLeps = [2, 3]
#         # nLeps = [3]
#         nJets = [2,3,4]
#         nMLJets = [1,2,3,4]
#         nBtags = [0,1,2]
#         # nBtags = [1,2]
#         numBins = (len(nMLJets)+len(nJets))*len(nBtags)
#         # numBins = (len(nMLJets))*len(nBtags)
#         nProc = ["signal", "rares", "fakes_mc", "flips_mc"]
#         numBackgrounds = len(nProc)-1
#         # systematicSources = ["LepSF","PU","Trigger","bTag","jes"]
#         # systematicSources = [   "pdf","LepSF","PU","Trigger","jes",
#         systematicSources = [   "LepSF","PU","Trigger","jes",
#                                 "lf","lfstats1","lfstats2",
#                                 "hf","hfstats1","hfstats2",
#                                 "cferr1","cferr2"]

#         #make some headers for my dataframe columns
#         dcColumns = []
#         binNames = []
#         binNamesObs = []
#         procNames = []
#         procIndex = []
#         for l in nLeps:
#             if l == 2:
#                 lep = "dilep"
#                 numJets = list(nJets)
#             if l == 3:
#                 lep = "trilep"
#                 numJets = list(nMLJets)
#             for j in numJets:
#                 for b in nBtags:
#                     counter = 0
#                     srName_base = lep+"_"+str(j)+"_"+str(b)
#                     binName = srName_base
#                     while len(binName) < 20:
#                         binName+=" "
#                     binNamesObs.append(binName)
#                     for p in nProc:
#                         srName = srName_base+"_"+p

#                         binNames.append(binName)

#                         while len(srName) < 20:
#                             srName+=" "
#                         dcColumns.append(srName)

#                         while len(p) < 20:
#                             p+=" "
#                         procNames.append(p)

#                         counterString = str(counter)
#                         while len(counterString) < 20:
#                             counterString+=" "
#                         procIndex.append(counterString)
#                         counter+=1

#         # ok, now I have headers, I can start making the titles for my rows
#         rowTitles = []
#         numParameters = 0
#         for p in nProc:
#             if p == "fakes_mc":
#                 iterator = 0
#                 for l in nLeps:
#                     if l == 2:
#                         lep = "dilep"
#                         numJets = list(nJets)
#                     if l == 3:
#                         lep = "trilep"
#                         numJets = list(nMLJets)
#                     for j in numJets:
#                         for b in nBtags:
#                             title = "fkStat"+yr+"_"+str(iterator)
#                             numParameters+=1
#                             yld = str(fakeCRStatYldDict[str(l)+"_"+str(j)+"_"+str(b)])
#                             while len(title) <(16-len(yld)):
#                                 title += " "
#                             title += "gmN "+yld
#                             rowTitles.append(title)
#                             iterator+=1
#             elif p == "flips_mc": 
#                 iterator = 0
#                 for l in nLeps:
#                     if l > 2: continue
#                     if l == 2:
#                         lep = "dilep"
#                         numJets = list(nJets)
#                     if l == 3:
#                         lep = "trilep"
#                         numJets = list(nMLJets)
#                     for j in numJets:
#                         for b in nBtags:
#                             # print(l, j, b, iterator)
#                             title = "flpSt"+yr+"_"+str(iterator)
#                             numParameters+=1
#                             yld = str(flipCRStatYldDict[str(l)+"_"+str(j)+"_"+str(b)])
#                             while len(title) <(16-len(yld)):
#                                 title += " "
#                             title += "gmN "+yld
#                             rowTitles.append(title)
#                             iterator+=1
#             else:
#                 iterator = 0
#                 while iterator < numBins:
#                     if p=="signal": title = "sig_stat_"+yr+"_"+str(iterator)
#                     else: title = p+"_stat_"+yr+"_"+str(iterator)
#                     # title = p+"_stat_"+yr+"_"+str(iterator)
#                     numParameters+=1
#                     while len(title) <17:
#                         title+=" "
#                     title+="lnN"
#                     rowTitles.append(title)
#                     iterator+=1
#             # print(rowTitles)

#         for p in nProc:
#             if "rares" in p: continue
#             if "signal" in p: continue
#             title = p+"_syst"
#             while len(title)<17:
#                 title+=" "
#             title+="lnN"
#             rowTitles.append(title)
#             numParameters+=1

#         title = "fakeRate_syst_"+yr
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         title = "flipRate_syst_"+yr
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         # title = "theory_"+yr
#         title = "theory_rare"
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         # title = "theory_"+yr
#         title = "theory_sig"
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         # title = "renorm_"+yr
#         title = "scaleShp_rare"
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         title = "scaleShp_sig"
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         title = "pdfShp"
#         while len(title)<17:
#             title+=" "
#         title+="lnN"
#         rowTitles.append(title)
#         numParameters+=1

#         for source in systematicSources:
#             if source == "PU" or source == "lf" or source == "hf" or "cferr" in source:
#                 title = source
#             else:
#                 title = source+"_"+yr
#             while len(title)<17:
#                 title+=" "
#             title+="lnN"
#             rowTitles.append(title)
#             numParameters+=1


#         #dataframe I will print to datacard file
#         dcard_df = pd.DataFrame(index = rowTitles, columns = dcColumns)
#         # print(dcColumns)
#         print("defined output dataframe")
#         # print(dcard_df)


#         #ok, now I want to know the stat uncertainty as a percentage of the yield
#         for p in nProc:
#             if p == "signal":
#                 proc = s
#             else:
#                 proc = p
#             statUnc = []
#             for l in nLeps:
#                 if l == 2:
#                     numJets = list(nJets)
#                 if l == 3:
#                     numJets = list(nMLJets)
#                 for j in numJets:
#                     for b in nBtags:
#                         # print (p, l, j, b)
#                         #calculate signal percentage for statistical unc.
#                         if proc == "fakes_mc":
#                             srbin = str(l)+"_"+str(j)+"_"+str(b)
#                             yld = fakeCRStatYldDict[srbin]
#                             row = fakeEst_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                             err = row["data estimate"].values[0]
#                             # err = row["fakes_mc"].values[0]
#                             # print(yld, err, err/yld)
#                         elif proc == "flips_mc":
#                             if l == 3:
#                                 continue
#                                 # yld = 0.0
#                                 # err = 0
#                             else:
#                                 srbin = str(l)+"_"+str(j)+"_"+str(b)
#                                 yld = flipCRStatYldDict[srbin]
#                                 row = flipEst_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                                 err = row["data estimate"].values[0]
#                                 # err = row["flips_mc"].values[0]
#                                 # print(yld, err, err/yld)
#                         elif proc == "rares":
#                             # print df
#                             # print df.loc[ (df["nLeptons"]==l) ]
#                             # print df.loc[ (df["nJets"]==j) ]
#                             # print df.loc[ (df["nBtags"]==b) ]
#                             row = df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                             # print row
#                             yld = row[proc].values[0]
#                             err = row[proc+" error"].values[0]
#                         else:
#                             # print df
#                             # print df.loc[ (df["nLeptons"]==l) ]
#                             # print df.loc[ (df["nJets"]==j) ]
#                             # print df.loc[ (df["nBtags"]==b) ]
#                             row = sig_df.loc[ (sig_df["nLeptons"]==l) & (sig_df["nJets"]==j) & (sig_df["nBtags"]==b) ]
#                             # print row
#                             yld = row[proc].values[0]
#                             err = row[proc+" error"].values[0]
                        
#                         if yld > 0:
#                             dcPercentage = round(err/yld,7)
#                         # else:
#                         #     dcPercentage = 1

#                         if dcPercentage>=1:
#                             dcPercentage = 1

#                         if proc == "fakes_mc": statUnc.append([l,j,b,dcPercentage])
#                         elif proc == "flips_mc": statUnc.append([l,j,b,dcPercentage])
#                         else: statUnc.append([l,j,b,1+dcPercentage])
#             # print(statUnc)
#             for i in range(len(statUnc)):
#                 lep = statUnc[i][0]
#                 if lep == 2: l = "dilep"
#                 if lep == 3: l = "trilep"
#                 jet = statUnc[i][1]
#                 btag = statUnc[i][2]
#                 unc = statUnc[i][3]

#                 cTitle = str(l)+"_"+str(jet)+"_"+str(btag)+"_"+p
#                 while len(cTitle) < 20:
#                     cTitle+=" "

#                 if p =="fakes_mc":
#                     rTitle = "fkStat"+yr+"_"+str(i)
#                     yld = str(fakeCRStatYldDict[str(lep)+"_"+str(jet)+"_"+str(btag)])
#                     # yld = str(fakeCRStatYld[i])
#                     while len(rTitle) <(16-len(yld)):
#                         rTitle += " "
#                     rTitle += "gmN "+yld
#                 elif p =="flips_mc":
#                     rTitle = "flpSt"+yr+"_"+str(i)
#                     yld = str(flipCRStatYldDict[str(lep)+"_"+str(jet)+"_"+str(btag)])
#                     # yld = str(flipCRStatYld[i])
#                     while len(rTitle) <(16-len(yld)):
#                         rTitle += " "
#                     rTitle += "gmN "+yld
#                 else:
#                     if p=="signal": rTitle = "sig_stat_"+yr+"_"+str(i)
#                     else: rTitle = p+"_stat_"+yr+"_"+str(i)
#                     # rTitle = p+"_stat_"+yr+"_"+str(i)
#                     while len(rTitle) < 17:
#                         rTitle+=" "
#                     rTitle+="lnN"
#                 #print("*************")
#                 # if p=="flips_mc":
#                 #     print(cTitle)
#                 #     print(rTitle)
#                 #     print(unc)


#                 for column in dcard_df:
#                     # print column
#                     if column==cTitle:
#                         filler = str(unc)
#                         while len(filler)<20:
#                             filler+=" "
#                         dcard_df.at[rTitle,column] = filler
#                         # if p=="flips_mc": print filler
#                         # if p=="flips_mc": print dcard_df.at[rTitle,column]
#                     else:
#                         filler = "-"
#                         while len(filler) < 20:
#                             filler += " "
#                         dcard_df.at[rTitle,column] = filler
#                         # print filler
#                 # if p == "flips_mc": print dcard_df
#         print("filled stat uncertainties")
#         #print(dcard_df)

#         #get MC yields in correct order of bins/processes
#         rates = []
#         observation = []
#         # if "tch" in s:
#         #     # h_obs = getObjFromFile("./outputs/oct7_runSR/pseudodata.root","h_tch_out_"+str(y))
#         #     h_obs = getObjFromFile("./outputs/oct7_runSR/pseudodata.root","h_tuh_out_"+str(y))
#         # elif "tuh" in s:
#         #     # h_obs = getObjFromFile("./outputs/oct7_runSR/pseudodata.root","h_tuh_out_"+str(y))
#         #     h_obs = getObjFromFile("./outputs/oct7_runSR/pseudodata.root","h_tch_out_"+str(y))
#         # for b in range(1,h_obs.GetNbinsX()+1):
#         #     observation.append(str(h_obs.GetBinContent(b)))
#         for l in nLeps:
#             if l == 2:
#                 numJets = list(nJets)
#             if l == 3:
#                 numJets = list(nMLJets)
#             # print(numJets)
#             for j in numJets:
#                 for b in nBtags:
#                     # # print fakeEst_df
#                     fakerow = fakeEst_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                     fliprow = flipEst_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                     sigrow  = sig_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                     row     = df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                     obsYld = row["rares"].values[0] + fakerow['data estimate'].values[0] + fliprow['data estimate'].values[0]
#                     # obsYld = row["rares"].values[0] + fakerow['fakes_mc'].values[0] + fliprow['flips_mc'].values[0]
#                     # if includeSignalInObs: obsYld += row[s].values[0]
#                     obsYld = round(obsYld,0)
#                     obsString = str(obsYld)
#                     while len(obsString)<20:
#                         obsString+=" "
#                     observation.append(obsString)

#                     for p in nProc:
#                         if p == "signal":
#                             p = s
#                             yld = sigrow[p].values[0]
#                         elif p == "fakes_mc":
#                             fakerow = fakeEst_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                             yld = fakerow["data estimate"].values[0]
#                             # yld = fakerow["fakes_mc"].values[0]
#                         elif p == "flips_mc":
#                             fliprow = flipEst_df.loc[ (df["nLeptons"]==l) & (df["nJets"]==j) & (df["nBtags"]==b) ]
#                             yld = fliprow["data estimate"].values[0]
#                             # yld = fliprow["flips_mc"].values[0]
#                         else:
#                             yld = row[p].values[0]

#                         # if yld<0:
#                         # if yld<=0:
#                         #     yld = 0.01

#                         yldString = str(yld)
#                         while len(yldString)<20:
#                             yldString+=" "
#                         rates.append(yldString)



#         #filling dummy systematic uncertainties
#         for p in nProc:
#             if "signal" in p:
#                 unc = "0.8/1.2"
#                 continue
#             if p == "flips_mc":
#                 # if y == 2016: unc = '1.1'
#                 # if y == 2017: unc = '1.4'
#                 # if y == 2018: unc = '1.3'
#                 unc = "0.7/1.3"
#             elif p == "rares":
#                 unc = "0.7/1.3"
#                 continue
#             elif p == "fakes_mc":
#                 unc = "0.6/1.4"

#             while len(unc)<20:
#                 unc+=" "
            
#             rTitle = p+"_syst"
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"

#             for column in dcard_df:
#                 if ((p in column) and not (p=="flips_mc" and "trilep" in column)):
#                     filler = unc
#                     while len(filler)<20:
#                         filler+=" "
#                     dcard_df.at[rTitle,column] = filler
#                 else:
#                     filler = "-"
#                     while len(filler) < 20:
#                         filler += " "
#                     dcard_df.at[rTitle,column] = filler

#         fakeRateIter = 0
#         for column in dcard_df:
#             rTitle = "fakeRate_syst_"+yr
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             if "fakes_mc" in column:
#                 filler = str(1+fakeSystErr[fakeRateIter]/100)
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column] = filler
#                 fakeRateIter+=1
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         flipRateIter = 0
#         for column in dcard_df:
#             rTitle = "flipRate_syst_"+yr
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             if "flips_mc" in column:
#                 if flipSystErr[flipRateIter]!=0:
#                     filler = str(1+flipSystErr[flipRateIter]/100)
#                 else: filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column] = filler
#                 flipRateIter+=1
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         for column in dcard_df:
#             rTitle = "theory_rare"
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             if("rares" in column):
#                 if "dilep" in column: l=2
#                 else: l=3
#                 srbin = column.split("_")
#                 j = int(srbin[1])
#                 b = int(srbin[2])
#                 filler = "1.25"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         for column in dcard_df:
#             rTitle = "theory_sig"
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             if ("signal" in column):
#                 if "dilep" in column: l=2
#                 else: l=3
#                 srbin = column.split("_")
#                 j = int(srbin[1])
#                 b = int(srbin[2])
#                 filler = str(round(1-float(theory_unc[str(y)][s.split("_")[1]][str(l)+"_"+str(j)+"_"+str(b)]["down"]),4))
#                 filler += "/"+str(round(1+float(theory_unc[str(y)][s.split("_")[1]][str(l)+"_"+str(j)+"_"+str(b)]["up"]),4))
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         srbinit = 0
#         rarebinit = 0
#         for column in dcard_df:
#             rTitle = "scaleShp_rare"
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             # if ("rares" in column):
#             if ("rares" in column):
#             # if ("signal" in column):
#                 if "dilep" in column: l=2
#                 else: l=3
#                 srbin = column.split("_")
#                 j = int(srbin[1])
#                 b = int(srbin[2])
#                 if "rares" in column:
#                     filler = raresShapeUnc[rarebinit]
#                     rarebinit +=1
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler
#                 # print(column, rTitle, filler, srbinit)
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         srbinit = 0
#         rarebinit = 0
#         for column in dcard_df:
#             rTitle = "scaleShp_sig"
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             # if ("rares" in column):
#             if("signal" in column):
#             # if ("signal" in column):
#                 if "dilep" in column: l=2
#                 else: l=3
#                 srbin = column.split("_")
#                 j = int(srbin[1])
#                 b = int(srbin[2])
#                 if s == "tuh":
#                     filler = tuhShapeUnc[srbinit]
#                 else:
#                     filler = tchShapeUnc[srbinit]
#                 srbinit+=1
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler
#                 # print(column, rTitle, filler, srbinit)
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         srbinit = 0
#         rarebinit = 0
#         for column in dcard_df:
#             rTitle = "pdfShp"
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             if ("signal" in column) or ("rares" in column):
#                 if "signal" in column:
#                     if "tch" in s:
#                         filler = tchPDFShapeUnc[srbinit]
#                     elif "tuh" in s:
#                         filler = tuhPDFShapeUnc[srbinit]
#                     srbinit+=1
#                 else:
#                     filler = raresPDFShapeUnc[rarebinit]
#                     rarebinit+=1
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler
#             else:
#                 filler = "-"
#                 while len(filler)<20:
#                     filler+=" "
#                 dcard_df.at[rTitle,column]=filler

#         # for column in dcard_df:
#         #     rTitle = "pdf_"+yr
#         #     while len(rTitle)<17:
#         #         rTitle+=" "
#         #     rTitle+="lnN"
#         #     if ("rares" in column):
#         #     # if ("rares" in column) or ("signal" in column):
#         #     # if ("signal" in column):
#         #         if "dilep" in column: l=2
#         #         else: l=3
#         #         srbin = column.split("_")
#         #         j = int(srbin[1])
#         #         b = int(srbin[2])
#         #         if "rares" in column:
#         #             row = raresSyst_df.loc[(raresSyst_df["nLeptons"]==l) & (raresSyst_df["nJets"]==j) & (raresSyst_df["nBtags"]==b)]
#         #             colTitleUp = "rares_pdf_up"
#         #             colTitleDown = "rares_pdf_down"
#         #             filler = str(round(row[colTitleDown],3))+"/"+str(round(row[colTitleUp],3))
#         #         # elif "signal" in column:
#         #         #     row = signalSyst_df.loc[(signalSyst_df["nLeptons"]==l) & (signalSyst_df["nJets"]==j) & (signalSyst_df["nBtags"]==b)]
#         #         #     colTitleUp = s+"_pdf_up"
#         #         #     colTitleDown = s+"_pdf_down"
#         #         #     filler = str(round(row[colTitleDown],3))+"/"+str(round(row[colTitleUp],3))
#         #         while len(filler)<20:
#         #             filler+=" "
#         #         dcard_df.at[rTitle,column]=filler
#         #     else:
#         #         filler = "-"
#         #         while len(filler)<20:
#         #             filler+=" "
#         #         dcard_df.at[rTitle,column]=filler

#         for source in systematicSources:
#             if source == "pdf": continue
#             if source == "PU" or source == "lf" or source == "hf" or "cferr" in source:
#                 rTitle = source
#             else:
#                 rTitle = source+"_"+yr
#             # rTitle = source+"_"+yr
#             while len(rTitle)<17:
#                 rTitle+=" "
#             rTitle+="lnN"
#             for column in dcard_df:
#                 if ("rares" in column) or ("signal" in column):
#                     if "dilep" in column: l=2
#                     else: l=3
#                     srbin = column.split("_")
#                     j = int(srbin[1])
#                     b = int(srbin[2])
#                     if "rares" in column:
#                         row = raresSyst_df.loc[(raresSyst_df["nLeptons"]==l) & (raresSyst_df["nJets"]==j) & (raresSyst_df["nBtags"]==b)]
#                         colTitleUp = "rares_"+source+"_up"
#                         colTitleDown = "rares_"+source+"_down"
#                         filler = str(round(row[colTitleDown],3))+"/"+str(round(row[colTitleUp],3))
#                         while len(filler)<20:
#                             filler+=" "
#                         dcard_df.at[rTitle,column]=filler
#                     elif "signal" in column:
#                         row = signalSyst_df.loc[(signalSyst_df["nLeptons"]==l) & (signalSyst_df["nJets"]==j) & (signalSyst_df["nBtags"]==b)]
#                         colTitleUp = s+"_"+source+"_up"
#                         colTitleDown = s+"_"+source+"_down"
#                         filler = str(round(row[colTitleDown],3))+"/"+str(round(row[colTitleUp],3))
#                         while len(filler)<20:
#                             filler+=" "
#                         dcard_df.at[rTitle,column]=filler
#                 else:
#                     filler = "-"
#                     while len(filler)<20:
#                         filler+=" "
#                     dcard_df.at[rTitle,column]=filler

#         print("filled syst uncertainties")
#         # print(dcard_df)


#         #define output file and write to output file
#         outfile = open(outdir+outfileName,"w")
#         binHeadersObs = "bin                 \t"
#         for b in binNamesObs:
#             binHeadersObs+=b
#             binHeadersObs+="\t"
#         binHeadersObs+="\n"
#         binHeaders = "bin                 \t"
#         for b in binNames:
#             binHeaders+=b
#             binHeaders+="\t"
#         binHeaders+="\n"
#         procHeaders = "process             \t"
#         for p in procNames:
#             procHeaders+=p
#             procHeaders+="\t"
#         procHeaders+="\n"
#         pInxHeaders = "process             \t"
#         for i in procIndex:
#             pInxHeaders+=i
#             pInxHeaders+="\t"
#         pInxHeaders+="\n"
#         rateHeaders = "rate                \t"
#         for r in rates:
#             rateHeaders+=r
#             rateHeaders+="\t"
#         rateHeaders+="\n"
#         obsHeaders = "observation         \t"
#         for o in observation:
#             obsHeaders+=o
#             obsHeaders+="\t"
#         obsHeaders+="\n"
#         imaxHeader = "imax "+str(numBins)+" number of channels\n"
#         jmaxHeader = "jmax "+str(numBackgrounds)+" number of backgrounds\n"
#         kmaxHeader = "kmax "+str(numParameters)+" number of nuisance parameters\n"
#         outfile.write(imaxHeader)
#         outfile.write(jmaxHeader)
#         outfile.write(kmaxHeader)
#         outfile.write("shapes * * FAKE\n\n")
#         outfile.write(binHeadersObs)
#         outfile.write(obsHeaders)
#         outfile.write("\n")
#         outfile.write(binHeaders)
#         outfile.write(procHeaders)
#         outfile.write(pInxHeaders)
#         outfile.write(rateHeaders)
#         outfile.write(dcard_df.to_csv(sep="\t", index=True, header=False))
#         outfile.close()
