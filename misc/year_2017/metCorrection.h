#include "metCorrectionTables.h"

std::pair<float,float> getCorrectMET(string fname, bool isData, int npv, float met, float phi){

    float metX = met * cos(phi);
    float metY = met * sin(phi);

    float Ax = getAx(fname, isData);
    float Ay = getAy(fname, isData);
    float Bx = getBx(fname, isData);
    float By = getBy(fname, isData);

    float metXcorr = -(Ax*npv + Bx);
    float metYcorr = -(Ay*npv + By);

    float corrected_x = metX+metXcorr;
    float corrected_y = metY+metYcorr;

    float correctedMET = sqrt((corrected_x*corrected_x)+(corrected_y*corrected_y));

    float correctedMETPhi;

    if(corrected_x==0 && corrected_y>0){correctedMETPhi = TMath::Pi();}
    else if(corrected_x==0 && corrected_y<0 )correctedMETPhi = -TMath::Pi();
    else if(corrected_x >0) correctedMETPhi = TMath::ATan(corrected_y/corrected_x);
    else if(corrected_x <0&& corrected_y>0) correctedMETPhi = TMath::ATan(corrected_y/corrected_x) + TMath::Pi();
    else if(corrected_x <0&& corrected_y<0) correctedMETPhi = TMath::ATan(corrected_y/corrected_x) - TMath::Pi();
    else correctedMETPhi =0;

    std::pair<float,float> correctedMET_METPhi(correctedMET,correctedMETPhi);
    return correctedMET_METPhi;

}
