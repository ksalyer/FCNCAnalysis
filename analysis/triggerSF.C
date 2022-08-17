#pragma GCC diagnostic ignored "-Wsign-compare"
#include "TFile.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TTree.h"
#include "TCanvas.h"
// #include "TChain.h"
#include "TTreeCache.h"
#include "TTreeCacheUnzip.h"
#include "TTreePerfStats.h"
#include "../../NanoTools/NanoCORE/SSSelections.h"
#include "../../NanoTools/NanoCORE/IsolationTools.h"
#include "../../NanoTools/NanoCORE/Nano.h"
#include "../../NanoTools/NanoCORE/Config.h"
#include "../../NanoTools/NanoCORE/Tools/goodrun.h"
#include "../../NanoTools/NanoCORE/Tools/dorky.h"
#include "../../NanoTools/NanoCORE/Tools/btagsf/BTagCalibrationStandalone.h"
#include "../../NanoTools/NanoCORE/Tools/btagsf/BTagCalibrationStandalone.cc"
#include "../misc/common_utils.h"
#include "../misc/year_run2/trigeffandsf.h"
#include <TROOT.h>
#include <TStyle.h>

#include <iostream>
#include <fstream>
#include <iomanip>


int triggerSF(std::string outputDir)
{
    gStyle->SetPaintTextFormat(".2f");
    gStyle->SetOptStat(0);
    
    TFile* f_trigEff = new TFile("/home/users/ksalyer/FCNCAnalysis/misc/year_run2/triggeffcymapsRA5_Run2_ALL.root");

    TFile outputRootFile(TString(outputDir+"/triggerSF.root").Data(),"RECREATE");

    std::vector<int> years = {2016, 2017, 2018};
    std::vector<std::string> year_str = {"2016", "2017", "2018"};

    // std::vector<int> years = {2016};
    // std::vector<std::string> year_str = {"2016"};

    Double_t ptBins_mu[11] = {20.,25.,30.,35.,40.,50.,75.,100.,200.,300.,500.};
    Double_t ptBins_mu_lead[10] = {25.,30.,35.,40.,50.,75.,100.,200.,300.,500.};
    Double_t etaBins_mu[6] = {0.,0.8,1.25,1.6,2.1,2.4};

    Double_t ptBins_el[11] = {20.,25.,30.,35.,40.,50.,75.,100.,200.,300.,500.};
    Double_t ptBins_el_lead[10] = {25.,30.,35.,40.,50.,75.,100.,200.,300.,500.};
    Double_t etaBins_el[5] = {0.,0.8,1.479,2,2.5};

    for (int y = 0; y < years.size(); y++){

        TH2D* el_el_1_hist = new TH2D(TString::Format("diel_leadleg_%s",year_str[y].c_str()).Data(),"diel_leadleg",9,ptBins_el_lead,4,etaBins_el);
        TH2D* el_el_2_hist = new TH2D(TString::Format("diel_subleadleg_%s",year_str[y].c_str()).Data(),"diel_subleadleg",10,ptBins_el,4,etaBins_el);

        TH2D* mu_mu_1_hist = new TH2D(TString::Format("dimu_leadleg_%s",year_str[y].c_str()).Data(),"dimu_leadleg",9,ptBins_mu_lead,5,etaBins_mu);
        TH2D* mu_mu_2_hist = new TH2D(TString::Format("dimu_subleadleg_%s",year_str[y].c_str()).Data(),"dimu_subleadleg",10,ptBins_mu,5,etaBins_mu);

        TH2D* mu_el_1_hist = new TH2D(TString::Format("muel_leadmu_%s",year_str[y].c_str()).Data(),"muel_leadmu",9,ptBins_mu_lead,5,etaBins_mu);
        TH2D* mu_el_2_hist = new TH2D(TString::Format("muel_subleadel_%s",year_str[y].c_str()).Data(),"muel_subleadel",10,ptBins_el,4,etaBins_el);

        TH2D* el_mu_1_hist = new TH2D(TString::Format("elmu_leadel_%s",year_str[y].c_str()).Data(),"elmu_leadel",9,ptBins_el_lead,4,etaBins_el);
        TH2D* el_mu_2_hist = new TH2D(TString::Format("elmu_subleadmu_%s",year_str[y].c_str()).Data(),"elmu_subleadmu",10,ptBins_mu,5,etaBins_mu);

        el_el_1_hist->SetMinimum(0.0);
        el_el_1_hist->SetMaximum(1.5);
        el_el_2_hist->SetMinimum(0.0);
        el_el_2_hist->SetMaximum(1.5);
        mu_mu_1_hist->SetMinimum(0.0);
        mu_mu_1_hist->SetMaximum(1.5);
        mu_mu_2_hist->SetMinimum(0.0);
        mu_mu_2_hist->SetMaximum(1.5);
        mu_el_1_hist->SetMinimum(0.0);
        mu_el_1_hist->SetMaximum(1.5);
        mu_el_2_hist->SetMinimum(0.0);
        mu_el_2_hist->SetMaximum(1.5);
        el_mu_1_hist->SetMinimum(0.0);
        el_mu_1_hist->SetMaximum(1.5);
        el_mu_2_hist->SetMinimum(0.0);
        el_mu_2_hist->SetMaximum(1.5);

        for (int p = 0; p < 10; p++){
            double elel1_pt = ((ptBins_el[p]+ptBins_el[p+1])/2)+1;
            double elel2_pt = ((ptBins_el[p]+ptBins_el[p+1])/2)-1;

            double mumu1_pt = ((ptBins_mu[p]+ptBins_mu[p+1])/2)+1;
            double mumu2_pt = ((ptBins_mu[p]+ptBins_mu[p+1])/2)-1;

            double muel1_pt = ((ptBins_mu[p]+ptBins_mu[p+1])/2)+1;
            double muel2_pt = ((ptBins_el[p]+ptBins_el[p+1])/2)-1;

            double elmu1_pt = ((ptBins_el[p]+ptBins_el[p+1])/2)+1;
            double elmu2_pt = ((ptBins_mu[p]+ptBins_mu[p+1])/2)-1;

            for (int el_eta = 0; el_eta < 4; el_eta++){
                std::string yearName;
                double sf=0.;
                double unc=0.;

                if(elel1_pt<25 && elel2_pt<25 && years[y]==2017) {yearName="2017CtoF";}
                else if(!(elel1_pt<25 && elel2_pt<25) && years[y]==2017) {yearName="2017BtoF";}
                else {yearName=year_str[y];}

                double elel1_eta = ((etaBins_el[el_eta]+etaBins_el[el_eta+1])/2);

                int elel1_xbin = el_el_1_hist->GetXaxis()->FindBin(elel1_pt);
                int elel1_ybin = el_el_1_hist->GetYaxis()->FindBin(elel1_eta);
                int elel1_bin = el_el_1_hist->GetBin(elel1_xbin,elel1_ybin);
                sf = LegEffcyorSF(f_trigEff,"ele23_diele",elel1_pt,elel1_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"ele23_diele",elel1_pt,elel1_eta,yearName,true,1));
                el_el_1_hist->SetBinContent(elel1_bin,sf);
                el_el_1_hist->SetBinError(elel1_bin,unc);

                double elel2_eta = ((etaBins_el[el_eta]+etaBins_el[el_eta+1])/2);

                int elel2_xbin = el_el_2_hist->GetXaxis()->FindBin(elel2_pt);
                int elel2_ybin = el_el_2_hist->GetYaxis()->FindBin(elel2_eta);
                int elel2_bin = el_el_2_hist->GetBin(elel2_xbin,elel1_ybin);
                sf = LegEffcyorSF(f_trigEff,"ele12_diele",elel2_pt,elel2_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"ele12_diele",elel2_pt,elel2_eta,yearName,true,1));
                el_el_2_hist->SetBinContent(elel2_bin,sf);
                el_el_2_hist->SetBinError(elel2_bin,unc);

                if(muel1_pt<25 && muel2_pt<25 && years[y]==2017) {yearName="2017CtoF";}
                else if(!(muel1_pt<25 && muel2_pt<25) && years[y]==2017) {yearName="2017BtoF";}
                else {yearName=year_str[y];}

                double muel2_eta = ((etaBins_el[el_eta]+etaBins_el[el_eta+1])/2);

                int muel2_xbin = mu_el_2_hist->GetXaxis()->FindBin(muel2_pt);
                int muel2_ybin = mu_el_2_hist->GetYaxis()->FindBin(muel2_eta);
                int muel2_bin = mu_el_2_hist->GetBin(muel2_xbin,muel2_ybin);
                sf = LegEffcyorSF(f_trigEff,"ele12_elemu",muel2_pt,muel2_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"ele12_elemu",muel2_pt,muel2_eta,yearName,true,1));
                mu_el_2_hist->SetBinContent(muel2_bin,sf);
                mu_el_2_hist->SetBinError(muel2_bin,unc);

                if(elmu1_pt<25 && elmu2_pt<25 && years[y]==2017) {yearName="2017CtoF";}
                else if(!(elmu1_pt<25 && elmu2_pt<25) && years[y]==2017) {yearName="2017BtoF";}
                else {yearName=year_str[y];}


                double elmu1_eta = ((etaBins_el[el_eta]+etaBins_el[el_eta+1])/2);

                int elmu1_xbin = el_mu_1_hist->GetXaxis()->FindBin(elmu1_pt);
                int elmu1_ybin = el_mu_1_hist->GetYaxis()->FindBin(elmu1_eta);
                int elmu1_bin = el_mu_1_hist->GetBin(elmu1_xbin,elmu1_ybin);
                sf = LegEffcyorSF(f_trigEff,"ele23_elemu",elmu1_pt,elmu1_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"ele23_elemu",elmu1_pt,elmu1_eta,yearName,true,1));
                el_mu_1_hist->SetBinContent(elmu1_bin,sf);
                el_mu_1_hist->SetBinError(elmu1_bin,unc);
            }

            for (int mu_eta = 0; mu_eta < 5; mu_eta++){
                std::string yearName;
                double sf=0.;
                double unc=0.;

                if(mumu1_pt<25 && mumu2_pt<25 && years[y]==2017) {yearName="2017CtoF";}
                else if(!(mumu1_pt<25 && mumu2_pt<25) && years[y]==2017) {yearName="2017BtoF";}
                else {yearName=year_str[y];}

                double mumu1_eta = ((etaBins_mu[mu_eta]+etaBins_mu[mu_eta+1])/2);

                int mumu1_xbin = mu_mu_1_hist->GetXaxis()->FindBin(mumu1_pt);
                int mumu1_ybin = mu_mu_1_hist->GetYaxis()->FindBin(mumu1_eta);
                int mumu1_bin = mu_mu_1_hist->GetBin(mumu1_xbin,mumu1_ybin);
                sf = LegEffcyorSF(f_trigEff,"mu17_dimu",mumu1_pt,mumu1_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"mu17_dimu",mumu1_pt,mumu1_eta,yearName,true,1));
                mu_mu_1_hist->SetBinContent(mumu1_bin,sf);
                mu_mu_1_hist->SetBinError(mumu1_bin,unc);

                double mumu2_eta = ((etaBins_mu[mu_eta]+etaBins_mu[mu_eta+1])/2);

                int mumu2_xbin = mu_mu_2_hist->GetXaxis()->FindBin(mumu2_pt);
                int mumu2_ybin = mu_mu_2_hist->GetYaxis()->FindBin(mumu2_eta);
                int mumu2_bin = mu_mu_2_hist->GetBin(mumu2_xbin,mumu2_ybin);
                sf = LegEffcyorSF(f_trigEff,"mu8_dimu",mumu2_pt,mumu2_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"mu8_dimu",mumu2_pt,mumu2_eta,yearName,true,1));
                mu_mu_2_hist->SetBinContent(mumu2_bin,sf);
                mu_mu_2_hist->SetBinError(mumu2_bin,unc);

                if(muel1_pt<25 && muel2_pt<25 && years[y]==2017) {yearName="2017CtoF";}
                else if(!(muel1_pt<25 && muel2_pt<25) && years[y]==2017) {yearName="2017BtoF";}
                else {yearName=year_str[y];}

                double muel1_eta = ((etaBins_mu[mu_eta]+etaBins_mu[mu_eta+1])/2);

                int muel1_xbin = mu_el_1_hist->GetXaxis()->FindBin(muel1_pt);
                int muel1_ybin = mu_el_1_hist->GetYaxis()->FindBin(muel1_eta);
                int muel1_bin = mu_el_1_hist->GetBin(muel1_xbin,muel1_ybin);
                sf = LegEffcyorSF(f_trigEff,"mu23_elemu",muel1_pt,muel1_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"mu23_elemu",muel1_pt,muel1_eta,yearName,true,1));
                mu_el_1_hist->SetBinContent(muel1_bin,sf);
                mu_el_1_hist->SetBinError(muel1_bin,unc);

                if(elmu1_pt<25 && elmu2_pt<25 && years[y]==2017) {yearName="2017CtoF";}
                else if(!(elmu1_pt<25 && elmu2_pt<25) && years[y]==2017) {yearName="2017BtoF";}
                else {yearName=year_str[y];}


                double elmu2_eta = ((etaBins_mu[mu_eta]+etaBins_mu[mu_eta+1])/2);

                int elmu2_xbin = el_mu_2_hist->GetXaxis()->FindBin(elmu2_pt);
                int elmu2_ybin = el_mu_2_hist->GetYaxis()->FindBin(elmu2_eta);
                int elmu2_bin = el_mu_2_hist->GetBin(elmu2_xbin,elmu2_ybin);
                sf = LegEffcyorSF(f_trigEff,"mu8_elemu",elmu2_pt,elmu2_eta,yearName,true,0);
                unc = fabs(sf - LegEffcyorSF(f_trigEff,"mu8_elemu",elmu2_pt,elmu2_eta,yearName,true,1));
                el_mu_2_hist->SetBinContent(elmu2_bin,sf);
                el_mu_2_hist->SetBinError(elmu2_bin,unc);

            }
        }

        outputRootFile.cd();
        el_el_1_hist->Write();
        el_el_2_hist->Write();
        mu_mu_1_hist->Write();
        mu_mu_2_hist->Write();
        mu_el_1_hist->Write();
        mu_el_2_hist->Write();
        el_mu_1_hist->Write();
        el_mu_2_hist->Write();
        auto c = new TCanvas("c", "c", 800, 600);
        c->cd();
        gPad->SetLogx();

        el_el_1_hist->GetXaxis()->SetTitle("p_{T}");
        el_el_1_hist->GetYaxis()->SetTitle("#eta");
        el_el_1_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elel1_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elel1_%s.pdf",year_str[y].c_str()).Data());

        el_el_2_hist->GetXaxis()->SetTitle("p_{T}");
        el_el_2_hist->GetYaxis()->SetTitle("#eta");
        el_el_2_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elel2_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elel2_%s.pdf",year_str[y].c_str()).Data());

        mu_mu_1_hist->GetXaxis()->SetTitle("p_{T}");
        mu_mu_1_hist->GetYaxis()->SetTitle("#eta");
        mu_mu_1_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/mumu1_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/mumu1_%s.pdf",year_str[y].c_str()).Data());

        mu_mu_2_hist->GetXaxis()->SetTitle("p_{T}");
        mu_mu_2_hist->GetYaxis()->SetTitle("#eta");
        mu_mu_2_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/mumu2_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/mumu2_%s.pdf",year_str[y].c_str()).Data());

        mu_el_1_hist->GetXaxis()->SetTitle("p_{T}");
        mu_el_1_hist->GetYaxis()->SetTitle("#eta");
        mu_el_1_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/muel1_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/muel1_%s.pdf",year_str[y].c_str()).Data());

        mu_el_2_hist->GetXaxis()->SetTitle("p_{T}");
        mu_el_2_hist->GetYaxis()->SetTitle("#eta");
        mu_el_2_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/muel2_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/muel2_%s.pdf",year_str[y].c_str()).Data());

        el_mu_1_hist->GetXaxis()->SetTitle("p_{T}");
        el_mu_1_hist->GetYaxis()->SetTitle("#eta");
        el_mu_1_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elmu1_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elmu1_%s.pdf",year_str[y].c_str()).Data());

        el_mu_2_hist->GetXaxis()->SetTitle("p_{T}");
        el_mu_2_hist->GetYaxis()->SetTitle("#eta");
        el_mu_2_hist->Draw("colz text e");
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elmu2_%s.png",year_str[y].c_str()).Data());
        c->SaveAs(TString::Format("/home/users/ksalyer/public_html/FCNC_plots/June26/elmu2_%s.pdf",year_str[y].c_str()).Data());

    }

    return 0;
}
