#pragma GCC diagnostic ignored "-Wsign-compare"
#include "TFile.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TChain.h"
#include "TTreeCache.h"
#include "TTreeCacheUnzip.h"
#include "TTreePerfStats.h"

#include "../../NanoTools/NanoCORE/Nano.h"
#include "../../NanoTools/NanoCORE/MetSelections.h"
#include "../../NanoTools/NanoCORE/Tools/JetCorrector.h"
#include "../../NanoTools/NanoCORE/tqdm.h"
#include "../../NanoTools/NanoCORE/Config.h"
#include "../../NanoTools/NanoCORE/SSSelections.h"

#include <TROOT.h>
#include <TStyle.h>

#include <iostream>
#include <iomanip>

// #define DEBUG

struct debugger { template<typename T> debugger& operator , (const T& v) { cerr<<v<<" "; return *this; } } dbg;
#ifdef DEBUG
    #define debug(args...) do {cerr << #args << ": "; dbg,args; cerr << endl;} while(0)
#else
    #define debug(args...)
#endif

using namespace std;
using namespace tas;

int ScanChain(TChain *ch, string procName, string year, int nevents_to_process=-1)
{
    cout << "entered scanchain function" << endl;
    int nEventsTotal = 0;
    int nEventsChain = ch->GetEntries();
    cout << "num chain events: " << nEventsChain << endl;
    TFile *currentFile = 0;
    TObjArray *listOfFiles = ch->GetListOfFiles();
    TIter fileIter(listOfFiles);
    tqdm bar;

    TFile* eff_output = new TFile(TString::Format("muonSFEff/muonSFEff_%s_%s.root",procName.c_str(),year.c_str()).Data(), "recreate");

    gStyle->SetPaintTextFormat(".2f");

    Double_t ptbins[9] = {20., 30., 50., 70., 100., 140., 200., 300., 600.};
    //Double_t ptbins[18] = {20., 25., 30., 35., 40., 45., 50., 60., 70., 80., 90., 100., 120., 150., 200., 300., 400., 600.};
    Double_t etabins[7] = {0., 0.4, 0.8, 1.2, 1.6, 2., 2.5};

    TH2D* h2_MuonEff_Denom = new TH2D("h2_Muon_Denom", TString::Format("lepton efficiency, Denominator, MC, #eta vs p_{T}").Data(), 8, ptbins, 6, etabins);
    TH2D* h2_MuonEff_Num = new TH2D("h2_Muon_Num", TString::Format("lepton efficiency, Numerator, MC, #eta vs p_{T}").Data(), 8, ptbins, 6, etabins);
    TH2D* h2_MuonEff_Eff = new TH2D("h2_Muon_Eff", TString::Format("lepton efficiency, MC, #eta vs p_{T}").Data(), 8, ptbins, 6, etabins);
    TH2D* h2_ElectronEff_Denom = new TH2D("h2_Electron_Denom", TString::Format("lepton efficiency, Denominator, MC, #eta vs p_{T}").Data(), 8, ptbins, 6, etabins);
    TH2D* h2_ElectronEff_Num = new TH2D("h2_Electron_Num", TString::Format("lepton efficiency, Numerator, MC, #eta vs p_{T}").Data(), 8, ptbins, 6, etabins);
    TH2D* h2_ElectronEff_Eff = new TH2D("h2_Electron_Eff", TString::Format("lepton efficiency, MC, #eta vs p_{T}").Data(), 8, ptbins, 6, etabins);
    
    // TH1D* h1_MuonEff_pt_Denom = new TH1D("h1_Muon_pt_Denom", TString::Format("lepton efficiency, Denominator, MC, p_{T}").Data(), 8, ptbins);
    // TH1D* h1_MuonEff_pt_Num = new TH1D("h1_Muon_pt_Num", TString::Format("lepton efficiency, Numerator, MC, p_{T}").Data(), 8, ptbins);
    TH1D* h1_MuonEff_pt_Eff = new TH1D("h1_Muon_pt_Eff", TString::Format("lepton efficiency, MC, p_{T}").Data(), 8, ptbins);

    // TH1D* h1_MuonEff_eta_Denom = new TH1D("h1_Muon_eta_Denom", TString::Format("lepton efficiency, Denominator, MC, #eta").Data(), 6, etabins);
    // TH1D* h1_MuonEff_eta_Num = new TH1D("h1_Muon_eta_Num", TString::Format("lepton efficiency, Numerator, MC, #eta").Data(), 6, etabins);
    TH1D* h1_MuonEff_eta_Eff = new TH1D("h1_Muon_eta_Eff", TString::Format("lepton efficiency, MC, #eta").Data(), 6, etabins);

    // TH1D* h1_ElectronEff_pt_Denom = new TH1D("h1_Electron_pt_Denom", TString::Format("lepton efficiency, Denominator, MC, p_{T}").Data(), 8, ptbins);
    // TH1D* h1_ElectronEff_pt_Num = new TH1D("h1_Electron_pt_Num", TString::Format("lepton efficiency, Numerator, MC, p_{T}").Data(), 8, ptbins);
    TH1D* h1_ElectronEff_pt_Eff = new TH1D("h1_Electron_pt_Eff", TString::Format("lepton efficiency, MC, p_{T}").Data(), 8, ptbins);

    // TH1D* h1_ElectronEff_eta_Denom = new TH1D("h1_Electron_eta_Denom", TString::Format("lepton efficiency, Denominator, MC, #eta").Data(), 6, etabins);
    // TH1D* h1_ElectronEff_eta_Num = new TH1D("h1_Electron_eta_Num", TString::Format("lepton efficiency, Numerator, MC, #eta").Data(), 6, etabins);
    TH1D* h1_ElectronEff_eta_Eff = new TH1D("h1_Electron_eta_Eff", TString::Format("lepton efficiency, MC, #eta").Data(), 6, etabins);
    
    h2_MuonEff_Denom->Sumw2();
    h2_MuonEff_Num->Sumw2();
    h2_MuonEff_Eff->Sumw2();    
    h2_ElectronEff_Denom->Sumw2();
    h2_ElectronEff_Num->Sumw2();
    h2_ElectronEff_Eff->Sumw2();

    // h1_MuonEff_pt_Denom->Sumw2();
    // h1_MuonEff_pt_Num->Sumw2();
    // h1_MuonEff_pt_Eff->Sumw2();

    // h1_MuonEff_eta_Denom->Sumw2();
    // h1_MuonEff_eta_Num->Sumw2();
    // h1_MuonEff_eta_Eff->Sumw2();

    // h1_ElectronEff_pt_Denom->Sumw2();
    // h1_ElectronEff_pt_Num->Sumw2();
    // h1_ElectronEff_pt_Eff->Sumw2();

    // h1_ElectronEff_eta_Denom->Sumw2();
    // h1_ElectronEff_eta_Num->Sumw2();
    // h1_ElectronEff_eta_Eff->Sumw2();

    while ( (currentFile = (TFile*)fileIter.Next()) )
    {
        TFile *file = TFile::Open( currentFile->GetTitle() );
        TTree *tree = (TTree*)file->Get("Events");
        TString filename(currentFile->GetTitle());

        tree->SetCacheSize(32*1024*1024);
        tree->SetCacheLearnEntries(100);

        nt.Init(tree);

        // Set up the NanoCORE's common configuration service tool
        gconf.GetConfigs(nt.year());

        for( unsigned int event = 0; event < tree->GetEntriesFast(); ++event)
        {

            nt.GetEntry(event);
            tree->LoadTree(event);

            nEventsTotal++;
            bar.progress(nEventsTotal, nEventsChain);

            Leptons leptons = getLeptons();
            int nLeps = leptons.size();
            for (auto lep : leptons){
                if (lep.absid()==11 && lep.pt()>20 && abs(lep.eta())<2.4 && !lep.isFake() && !lep.isFlip()){
                    h2_ElectronEff_Denom->Fill(lep.pt(),abs(lep.eta()));
                    // h1_ElectronEff_pt_Denom->Fill(lep.pt());
                    // h1_ElectronEff_eta_Denom->Fill(abs(lep.eta()));
                    if (lep.idlevel()==SS::IDLevel::IDtight){
                        h2_ElectronEff_Num->Fill(lep.pt(),abs(lep.eta()));
                        // h1_ElectronEff_pt_Num->Fill(lep.pt());
                        // h1_ElectronEff_eta_Num->Fill(abs(lep.eta()));
                    }
                }else if (lep.absid()==13 && lep.pt()>20 && abs(lep.eta())<2.5 && !lep.isFake() && !lep.isFlip()){
                    h2_MuonEff_Denom->Fill(lep.pt(),abs(lep.eta()));
                    // h1_MuonEff_pt_Denom->Fill(lep.pt());
                    // h1_MuonEff_eta_Denom->Fill(abs(lep.eta()));
                    if (lep.idlevel()==SS::IDLevel::IDtight){
                        h2_MuonEff_Num->Fill(lep.pt(),abs(lep.eta()));
                        // h1_MuonEff_pt_Num->Fill(lep.pt());
                        // h1_MuonEff_eta_Num->Fill(abs(lep.eta()));
                    }
                }
            }

            if (nevents_to_process > 0 and nEventsTotal > nevents_to_process) break;
        }
        if (nevents_to_process > 0 and nEventsTotal > nevents_to_process) break;

        delete file;

    }

    h2_ElectronEff_Eff->Divide(h2_ElectronEff_Num, h2_ElectronEff_Denom, 1, 1, "B");
    h2_MuonEff_Eff->Divide(h2_MuonEff_Num, h2_MuonEff_Denom, 1, 1, "B");

    // h1_ElectronEff_pt_Eff->Divide(h1_ElectronEff_pt_Num, h1_ElectronEff_pt_Denom, 1, 1, "B");
    // h1_MuonEff_pt_Eff->Divide(h1_MuonEff_pt_Num, h1_MuonEff_pt_Denom, 1, 1, "B");
    // h1_ElectronEff_eta_Eff->Divide(h1_ElectronEff_eta_Num, h1_ElectronEff_eta_Denom, 1, 1, "B");
    // h1_MuonEff_eta_Eff->Divide(h1_MuonEff_eta_Num, h1_MuonEff_eta_Denom, 1, 1, "B");

    TH1D* h1_MuonEff_pt_Denom = h2_MuonEff_Denom->ProjectionX();
    TH1D* h1_MuonEff_pt_Num = h2_MuonEff_Num->ProjectionX();
    // TH1D* h1_MuonEff_pt_Eff = h2_MuonEff_Num->Divide(h1_MuonEff_pt_Denom);

    TH1D* h1_MuonEff_eta_Denom = h2_MuonEff_Denom->ProjectionY();
    TH1D* h1_MuonEff_eta_Num = h2_MuonEff_Num->ProjectionY();
    // TH1D* h1_MuonEff_eta_Eff = h2_MuonEff_Num->Divide(h1_MuonEff_eta_Denom);

    TH1D* h1_ElectronEff_pt_Denom = h2_ElectronEff_Denom->ProjectionX();
    TH1D* h1_ElectronEff_pt_Num = h2_ElectronEff_Num->ProjectionX();
    // TH1D* h1_ElectronEff_pt_Eff = h2_ElectronEff_Num->Divide(h1_ElectronEff_pt_Denom);

    TH1D* h1_ElectronEff_eta_Denom = h2_ElectronEff_Denom->ProjectionY();
    TH1D* h1_ElectronEff_eta_Num = h2_ElectronEff_Num->ProjectionY();
    // TH1D* h1_ElectronEff_eta_Eff = h2_ElectronEff_Num->Divide(h1_ElectronEff_eta_Denom);

    h1_ElectronEff_pt_Eff->Divide(h1_ElectronEff_pt_Num, h1_ElectronEff_pt_Denom, 1, 1, "B");
    h1_MuonEff_pt_Eff->Divide(h1_MuonEff_pt_Num, h1_MuonEff_pt_Denom, 1, 1, "B");
    h1_ElectronEff_eta_Eff->Divide(h1_ElectronEff_eta_Num, h1_ElectronEff_eta_Denom, 1, 1, "B");
    h1_MuonEff_eta_Eff->Divide(h1_MuonEff_eta_Num, h1_MuonEff_eta_Denom, 1, 1, "B");

    auto c = new TCanvas("c", "c", 800, 600);
    c->cd();

    gStyle->SetPaintTextFormat(".2f");
    gStyle->SetOptStat(0);
    gPad->SetLogx();
    
    h2_ElectronEff_Eff->SetMinimum(0.0);
    h2_ElectronEff_Eff->SetMaximum(1.0);
    h2_ElectronEff_Eff->Draw("colz text");
    c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June28/el_eff_%s_%s.png",procName.c_str(),year.c_str()).Data());
    c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June28/el_eff_%s_%s.pdf",procName.c_str(),year.c_str()).Data());
    
    h2_MuonEff_Eff->SetMinimum(0.0);
    h2_MuonEff_Eff->SetMaximum(1.0);
    h2_MuonEff_Eff->Draw("colz text");
    c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June28/mu_eff_%s_%s.png",procName.c_str(),year.c_str()).Data());
    c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June28/mu_eff_%s_%s.pdf",procName.c_str(),year.c_str()).Data());

    eff_output->cd();
    h2_ElectronEff_Denom->Write();
    h2_MuonEff_Denom->Write();
    h2_ElectronEff_Num->Write();
    h2_MuonEff_Num->Write();
    h2_ElectronEff_Eff->Write();
    h2_MuonEff_Eff->Write();

    h1_ElectronEff_pt_Denom->Write();
    h1_MuonEff_pt_Denom->Write();
    h1_ElectronEff_pt_Num->Write();
    h1_MuonEff_pt_Num->Write();
    h1_ElectronEff_pt_Eff->Write();
    h1_MuonEff_pt_Eff->Write();

    h1_ElectronEff_eta_Denom->Write();
    h1_MuonEff_eta_Denom->Write();
    h1_ElectronEff_eta_Num->Write();
    h1_MuonEff_eta_Num->Write();
    h1_ElectronEff_eta_Eff->Write();
    h1_MuonEff_eta_Eff->Write();

    eff_output->Close();
    bar.finish();

    return 0;
}
