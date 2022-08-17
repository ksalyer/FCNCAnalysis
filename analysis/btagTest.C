
// #include "../../NanoTools/NanoCORE/Tools/btagsf/BTagCalibrationStandalone.h"
// #include "../../NanoTools/NanoCORE/Tools/btagsf/BTagCalibrationStandalone.cc"
#include "CondFormats/BTauObjects/interface/BTagCalibration.h"
#include "CondTools/BTau/interface/BTagCalibrationReader.h"


using namespace std;
using namespace std::chrono;


void btagTest(){
	//b discriminator reshaping
    string csv_path_2016 = "/home/users/ksalyer/NanoTools/NanoCORE/Tools/btagsf/csv/DeepJet_2016LegacySF_V1.csv";
    cout << "got paths" << endl;

    BTagCalibration deepjet_csv_2016 = BTagCalibration("csvv1", csv_path_2016);
    cout << "loaded calibration" << endl;

    BTagCalibrationReader deepjet_medium_reader_2016 = BTagCalibrationReader(BTagEntry::OP_RESHAPING,
        "central",
        {"up_hf"}
        // {"up_lf","down_lf",
        // "up_hf","down_hf",
        // "up_hfstats1","down_hfstats1",
        // "up_hfstats2","down_hfstats2",
        // "up_lfstats1","down_lfstats1",
        // "up_lfstats2","down_lfstats2",
        // "up_cferr1","down_cferr1",
        // "up_cferr2","down_cferr2"}
        );
    BTagCalibrationReader up_reader_2016 = BTagCalibrationReader(BTagEntry::OP_RESHAPING,"up_hf");

    cout << "loaded OP and syst unc" << endl;

    deepjet_medium_reader_2016.load(deepjet_csv_2016, BTagEntry::FLAV_B, "iterativefit");
    deepjet_medium_reader_2016.load(deepjet_csv_2016, BTagEntry::FLAV_C, "iterativefit");
    deepjet_medium_reader_2016.load(deepjet_csv_2016, BTagEntry::FLAV_UDSG, "iterativefit");
    up_reader_2016.load(deepjet_csv_2016, BTagEntry::FLAV_B, "iterativefit");
    up_reader_2016.load(deepjet_csv_2016, BTagEntry::FLAV_C, "iterativefit");
    up_reader_2016.load(deepjet_csv_2016, BTagEntry::FLAV_UDSG, "iterativefit");
    cout << "loaded flavors for iterativefit" << endl;



    cout << "TESTING evaluation: " << up_reader_2016.eval_auto_bounds(  "up_hf",BTagEntry::FLAV_B,0.822876,91.875,0.970703) << endl;



}