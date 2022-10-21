//https://lathomas.web.cern.ch/lathomas/METStuff/XYCorrections/XYMETCorrection_withUL17andUL18andUL16.h

float getAx(string fname, bool isData) {
    if(isData){
        if(fname.find("2017B")!= std::string::npos){return -0.211161;}
        else if(fname.find("2017C")!= std::string::npos){return -0.185184;}
        else if(fname.find("2017D")!= std::string::npos){return -0.201606;}
        else if(fname.find("2017E")!= std::string::npos){return -0.162472;}
        else if(fname.find("2017F")!= std::string::npos){return -0.210639;}
        else{return 0;}
    }else{
        return -0.300155;
    }
}

float getAy(string fname, bool isData) {
    if(isData){
        if(fname.find("2017B")!= std::string::npos){return 0.251789;}
        else if(fname.find("2017C")!= std::string::npos){return 0.200941;}
        else if(fname.find("2017D")!= std::string::npos){return 0.188208;}
        else if(fname.find("2017E")!= std::string::npos){return 0.138076;}
        else if(fname.find("2017F")!= std::string::npos){return 0.198626;}
        else{return 0;}
    }else{
        return 0.300213;
    }
}

float getBx(string fname, bool isData) {
    if(isData){
        if(fname.find("2017B")!= std::string::npos){return 0.419333;}
        else if(fname.find("2017C")!= std::string::npos){return -0.164009;}
        else if(fname.find("2017D")!= std::string::npos){return 0.426502;}
        else if(fname.find("2017E")!= std::string::npos){return 0.176329;}
        else if(fname.find("2017F")!= std::string::npos){return 0.72934;}
        else{return 0;}
    }else{
        return 1.90608;
    }
}

float getBy(string fname, bool isData) {
    if(isData){
        if(fname.find("2017B")!= std::string::npos){return -1.28089;}
        else if(fname.find("2017C")!= std::string::npos){return -0.56853;}
        else if(fname.find("2017D")!= std::string::npos){return -0.58313;}
        else if(fname.find("2017E")!= std::string::npos){return -0.250239;}
        else if(fname.find("2017F")!= std::string::npos){return 1.028;}
        else{return 0;}
    }else{
        return -2.02232;
    }
}