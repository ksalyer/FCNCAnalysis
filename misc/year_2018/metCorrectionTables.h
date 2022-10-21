float getAx(string fname, bool isData) {
    if(isData){
        if(fname.find("2018A")!= std::string::npos){return 0.263733;}
        else if(fname.find("2018B")!= std::string::npos){return 0.400466;}
        else if(fname.find("2018C")!= std::string::npos){return 0.430911;}
        else if(fname.find("2018D")!= std::string::npos){return 0.457327;}
        else{return 0;}
    }else{
        return 0.183518;
    }
}

float getAy(string fname, bool isData) {
    if(isData){
        if(fname.find("2018A")!= std::string::npos){return 0.0431304;}
        else if(fname.find("2018B")!= std::string::npos){return 0.146125;}
        else if(fname.find("2018C")!= std::string::npos){return 0.0620083;}
        else if(fname.find("2018D")!= std::string::npos){return 0.0684071;}
        else{return 0;}
    }else{
        return 0.192263;
    }
}

float getBx(string fname, bool isData) {
    if(isData){
        if(fname.find("2018A")!= std::string::npos){return -1.91115;}
        else if(fname.find("2018B")!= std::string::npos){return -3.05914;}
        else if(fname.find("2018C")!= std::string::npos){return -1.42865;}
        else if(fname.find("2018D")!= std::string::npos){return -1.56856;}
        else{return 0;}
    }else{
        return 0.546754;
    }
}

float getBy(string fname, bool isData) {
    if(isData){
        if(fname.find("2018A")!= std::string::npos){return -0.112043;}
        else if(fname.find("2018B")!= std::string::npos){return -0.533233;}
        else if(fname.find("2018C")!= std::string::npos){return -1.46021;}
        else if(fname.find("2018D")!= std::string::npos){return -0.928372;}
        else{return 0;}
    }else{
        return -0.42121;
    }
}