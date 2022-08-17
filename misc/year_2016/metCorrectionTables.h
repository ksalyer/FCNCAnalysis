float getAx(string fname, bool isData) {
    if(isData){
        return 0;
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
        return 0;
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
        return 0;
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
        return 0;
    }else{
        if(fname.find("NonAPV")!= std::string::npos){
            return -0.243323;
        }else{
            return -0.117747;
        }
    }
}