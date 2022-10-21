float getAx(string fname, bool isData) {
    if(isData){
        if(fname.find("2016B")!= std::string::npos){return -0.0214894;}
        else if(fname.find("2016C")!= std::string::npos){return -0.032209;}
        else if(fname.find("2016D")!= std::string::npos){return -0.0293663;}
        else if(fname.find("2016E")!= std::string::npos){return -0.0132046;}
        else if(fname.find("2016F")!= std::string::npos){return -0.0543566;}
        else if(fname.find("2016G")!= std::string::npos){return 0.121809;}
        else if(fname.find("2016H")!= std::string::npos){return 0.0868828;}
        else{return 0;}
    }else{
        if(fname.find("NonAPV")!= std::string::npos){
            return -0.153497;
        }else{
            return -0.188743;
        }
    }
}

float getAy(string fname, bool isData) {
    if(isData){
        if(fname.find("2016B")!= std::string::npos){return 0.0876624;}
        else if(fname.find("2016C")!= std::string::npos){return 0.113917;}
        else if(fname.find("2016D")!= std::string::npos){return 0.11331;}
        else if(fname.find("2016E")!= std::string::npos){return 0.134809;}
        else if(fname.find("2016F")!= std::string::npos){return 0.114225;}
        else if(fname.find("2016G")!= std::string::npos){return 0.0558974;}
        else if(fname.find("2016H")!= std::string::npos){return 0.0888774;}
        else{return 0;}
    }else{
        if(fname.find("NonAPV")!= std::string::npos){
            return 0.00731978;
        }else{
            return 0.0127927;
        }
    }
}

float getBx(string fname, bool isData) {
    if(isData){
        if(fname.find("2016B")!= std::string::npos){return -0.188255;}
        else if(fname.find("2016C")!= std::string::npos){return 0.067288;}
        else if(fname.find("2016D")!= std::string::npos){return 0.21106;}
        else if(fname.find("2016E")!= std::string::npos){return 0.20073;}
        else if(fname.find("2016F")!= std::string::npos){return 0.816597;}
        else if(fname.find("2016G")!= std::string::npos){return -0.584893;}
        else if(fname.find("2016H")!= std::string::npos){return -0.703489;}
        else{return 0;}
    }else{
        if(fname.find("NonAPV")!= std::string::npos){
            return 0.231751;
        }else{
            return -0.136539;
        }
    }
}

float getBy(string fname, bool isData) {
    if(isData){
        if(fname.find("2016B")!= std::string::npos){return 0.812885;}
        else if(fname.find("2016C")!= std::string::npos){return 0.743906;}
        else if(fname.find("2016D")!= std::string::npos){return 0.815787;}
        else if(fname.find("2016E")!= std::string::npos){return 0.679068;}
        else if(fname.find("2016F")!= std::string::npos){return 1.17266;}
        else if(fname.find("2016G")!= std::string::npos){return 0.891234;}
        else if(fname.find("2016H")!= std::string::npos){return 0.902632;}
        else{return 0;}
    }else{
        if(fname.find("NonAPV")!= std::string::npos){
            return -0.243323;
        }else{
            return -0.117747;
        }
    }
}