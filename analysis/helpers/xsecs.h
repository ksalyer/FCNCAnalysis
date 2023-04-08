std::string short_to_long (std::string sampleName, int year) {
    std::map< std::string, std::string > m_short_to_long;
    //2016
    m_short_to_long["dyjets_m50_2016"] = "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1_NANOAODSIM";
    m_short_to_long["dyjets_m10-50_2016"] = "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_2016"] = "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1_NANOAODSIM";
    m_short_to_long["ttjets_2016"] = "TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tt1lep_2016"] = "TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tt2lep_2016"] = "TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["ttw_2016"] = "TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1_NANOAODSIM";
    m_short_to_long["ttz_m10_2016"] = "TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext3-v1_NANOAODSIM";
    m_short_to_long["ttz_m1-10_2016"] = "TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tth_nobb_2016"] = "ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tzq_2016"] = "tZq_ll_4f_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["tttt_2016"] = "TTTT_TuneCUETP8M2T4_PSweights_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tg_2016"] = "TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttg_1lep_2016"] = "TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["ttg_dilep_2016"] = "TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wg_2016"] = "WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext3-v1_NANOAODSIM";
    m_short_to_long["zg_2016"] = "ZGToLLG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wz_2016"] = "WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ggh_2016"] = "GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tw_dilep_2016"] = "ST_tWll_5f_LO_13TeV-MadGraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tw_top_2016"] = "ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tw_atop_2016"] = "ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hct_ST_2016"] = "ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hut_ST_2016"] = "ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hct_atop_2016"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hut_atop_2016"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hct_top_2016"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hut_top_2016"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["tthh_2016"] = "TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["tttj_2016"] = "TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["tttw_2016"] = "TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttwh_2016"] = "TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttww_2016"] = "TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttwz_2016"] = "TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttzh_2016"] = "TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttzz_2016"] = "TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["vh_nobb_2016"] = "VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_ht100-200_2016"] = "WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1_NANOAODSIM";
    m_short_to_long["wjets_ht200-400_2016"] = "WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext2-v1_NANOAODSIM";
    m_short_to_long["wjets_ht400-600_2016"] = "WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["wjets_ht600-800_2016"] = "WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["wjets_ht800-1200_2016"] = "WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["qqww_2016"] = "WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wwg_2016"] = "WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ww_2016"] = "WWTo2L2Nu_DoubleScattering_13TeV-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["www_2016"] = "WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wwz_2016"] = "WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wzg_2016"] = "WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["wzz_2016"] = "WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["zz_2016"] = "ZZTo4L_13TeV_powheg_pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    m_short_to_long["zzz_2016"] = "ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8-v1_NANOAODSIM";
    

    //2017
    m_short_to_long["dyjets_m10-50_2017"] = "DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["dyjets_m50_2017"] = "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017RECOSIMstep_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ggh_2017"] = "GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext3-v1_NANOAODSIM";
    m_short_to_long["tw_dilep_2017"] = "ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["tw_top_2017"] = "ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tw_atop_2017"] = "ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tg_2017"] = "TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    //m_short_to_long["signal_hct_atop_2017"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    //m_short_to_long["signal_hut_atop_2017"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    //m_short_to_long["signal_hct_top_2017"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    //m_short_to_long["signal_hut_top_2017"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hct_ST_2017"] = "ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_tauDecays_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hut_ST_2017"] = "ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_tauDecays_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hct_atop_2017"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hct_TuneCP5-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_tauDecays_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hut_atop_2017"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hut_TuneCP5-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_tauDecays_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hct_top_2017"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hct_TuneCP5-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_tauDecays_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["signal_hut_top_2017"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hut_TuneCP5-MadGraph5-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_tauDecays_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttg_dilep_2017"] = "TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttg_1lep_2017"] = "TTGamma_SingleLept_TuneCP5_PSweights_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tthh_2017"] = "TTHH_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v2_NANOAODSIM";
    m_short_to_long["tth_nobb_2017"] = "ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttjets_2017"] = "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tt1lep_2017"] = "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tt2lep_2017"] = "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tttj_2017"] = "TTTJ_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tttt_2017"] = "TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tttw_2017"] = "TTTW_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttwh_2017"] = "TTWH_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttw_2017"] = "TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttww_2017"] = "TTWW_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["ttwz_2017"] = "TTWZ_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttzh_2017"] = "TTZH_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttz_m1-10_2017"] = "TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttz_m10_2017"] = "TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ttzz_2017"] = "TTZZ_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["tzq_2017"] = "tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["vh_nobb_2017"] = "VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wg_2017"] = "WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_ht100-200_2017"] = "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_ht200-400_2017"] = "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_ht400-600_2017"] = "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_ht600-800_2017"] = "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_ht800-1200_2017"] = "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wjets_2017"] = "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8_ext1-v1_NANOAODSIM";
    m_short_to_long["qqww_2017"] = "WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wwg_2017"] = "WWG_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["ww_2017"] = "WWTo2L2Nu_DoubleScattering_13TeV-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["www_2017"] = "WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wwz_2017"] = "WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wzg_2017"] = "WZG_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wz_2017"] = "WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["wzz_2017"] = "WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["zg_2017"] = "ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["zz_2017"] = "ZZTo4L_13TeV_powheg_pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    m_short_to_long["zzz_2017"] = "ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1_NANOAODSIM";
    

    //2018
    m_short_to_long["dyjets_m50_2018"] = "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["ttw_2018"] = "TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["www_2018"] = "WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["signal_hct_ST_2018"] = "ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_tauDecays_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["signal_hut_ST_2018"] = "ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_tauDecays_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["signal_hut_atop_2018"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hut_TuneCP5-MadGraph5-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_tauDecays_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["signal_hut_top_2018"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hut_TuneCP5-MadGraph5-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_tauDecays_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["signal_hct_atop_2018"] = "TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hct_TuneCP5-MadGraph5-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_tauDecays_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["signal_hct_top_2018"] = "TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hct_TuneCP5-MadGraph5-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_tauDecays_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["wjets_ht800-1200_2018"] = "WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["wjets_ht600-800_2018"] = "WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["wzz_2018"] = "WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["wz_2018"] = "WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["tg_2018"] = "TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["wzg_2018"] = "WZG_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tth_nobb_2018"] = "ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["ttg_dilep_2018"] = "TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tttj_2018"] = "TTTJ_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttjets_2018"] = "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1_NANOAODSIM";
    m_short_to_long["tt1lep_2018"] = "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tt2lep_2018"] = "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tttt_2018"] = "TTTT_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1_NANOAODSIM";
    m_short_to_long["tttw_2018"] = "TTTW_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["wjets_ht100-200_2018"] = "WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tthh_2018"] = "TTHH_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["vh_nobb_2018"] = "VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["wjets_2018"] = "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["wjets_ht400-600_2018"] = "WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tzq_2018"] = "tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttwh_2018"] = "TTWH_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttg_1lep_2018"] = "TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["dyjets_m10-50_2018"] = "DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["zg_2018"] = "ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["wwz_2018"] = "WWZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["wwg_2018"] = "WWG_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttwz_2018"] = "TTWZ_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["zz_2018"] = "ZZTo4L_TuneCP5_13TeV_powheg_pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1_NANOAODSIM";
    m_short_to_long["ttww_2018"] = "TTWW_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext2-v1_NANOAODSIM";
    m_short_to_long["wjets_ht200-400_2018"] = "WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["wg_2018"] = "WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttz_m10_2018"] = "TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["qqww_2018"] = "WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["zzz_2018"] = "ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ww_2018"] = "WWTo2L2Nu_DoubleScattering_13TeV-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["data_2018"] = "";
    m_short_to_long["ggh_2018"] = "GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV7011_pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["ttzh_2018"] = "TTZH_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttz_m1-10_2018"] = "TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21-v1_NANOAODSIM";
    m_short_to_long["tw_dilep_2018"] = "ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["tw_top_2018"] = "ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT1_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["tw_atop_2018"] = "ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_EXT1_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";
    m_short_to_long["ttzz_2018"] = "TTZZ_TuneCP5_13TeV-madgraph-pythia8_RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1_NANOAODSIM";

    return m_short_to_long[sampleName+"_"+std::to_string(year)];
}

double getXSec( string sampleName ){

    map< string, double > xsecs;

    xsecs["tw_dilep"] = 0.01123;
    xsecs["tw_top"] = 19.47;
    xsecs["tw_atop"] = 19.47;
    xsecs["ttjets"] = 831.762;
    xsecs["tt1lep"] = 364.35;
    xsecs["tt2lep"] = 87.31;
    xsecs["tg"] = 2.967;
    xsecs["wg"] = 405.271;
    xsecs["wjets"] = 61334.9;
    xsecs["wwg"] = 0.2147;
    xsecs["ww"] = 0.16975;
    xsecs["www"] = 0.2086;
    xsecs["wwz"] = 0.1651;
    xsecs["wzg"] = 0.04123;
    xsecs["wz"] = 4.4297;
    xsecs["wzz"] = 0.05565;
    xsecs["qqww"] = 0.05390;
    xsecs["zg"] = 123.8;
    xsecs["zz"] = 1.256;
    xsecs["zzz"] = 0.01398;
    xsecs["ggh"] = 0.01181;
    xsecs["ttg_dilep"] = 0.632;
    xsecs["ttg_1lep"] = 0.77;
    xsecs["tthh"] = 0.000757;
    xsecs["tttj"] = 0.000474;
    xsecs["tttt"] = 0.01197;
    xsecs["tttw"] = 0.000788;
    xsecs["ttwh"] = 0.001582;
    xsecs["ttw"] = 0.2043;
    // xsecs["ttw"] = 0.2728;
    xsecs["ttww"] = 0.01150;
    xsecs["ttwz"] = 0.003884;
    xsecs["ttzh"] = 0.001535;
    xsecs["ttz_m10"] = 0.2529;
    xsecs["ttz_m1-10"] = 0.0493;
    xsecs["ttzz"] = 0.001982;
    xsecs["dyjets_m10-50"] = 18610;
    xsecs["dyjets_m50"] = 6020.85;
    xsecs["vh_nobb"] = 2.1360;
    xsecs["tzq"] = 0.0758;
    xsecs["tth_nobb"] = 0.2710;
    xsecs["signal_hct_ST"] = 6.99;
    xsecs["signal_hut_ST"] = 50.82;
    xsecs["signal_hct_atop"] = 83.88144;
    xsecs["signal_hut_atop"] = 83.88144;
    xsecs["signal_hct_top"] = 83.88144;
    xsecs["signal_hut_top"] = 83.88144;

    // xsecs["signal_hct_ST"] = 1.01;
    // xsecs["signal_hut_ST"] = 7.32;
    // xsecs["signal_hct_atop"] = 12.08;
    // xsecs["signal_hut_atop"] = 12.08;
    // xsecs["signal_hct_top"] = 12.08;
    // xsecs["signal_hut_top"] = 12.08;

    // xsecs["signal_hct_ST"] = 0.505;
    // xsecs["signal_hut_ST"] = 3.66;
    // xsecs["signal_hct_atop"] = 6.04;
    // xsecs["signal_hut_atop"] = 6.04;
    // xsecs["signal_hct_top"] = 6.04;
    // xsecs["signal_hut_top"] = 6.04;

    double xsecForWeight = xsecs[sampleName];

    return xsecForWeight;
}
