from cc_corpus import CC_Corpus
import random

#Initialize
cc = CC_Corpus()

#Define the temp s3 bucket
write_bucket = "ccglu1"

#Define prefix from the Common Crawl
prefix_list = [
		"CC-MAIN-2015-06", "CC-MAIN-2015-11",
		"CC-MAIN-2015-14", "CC-MAIN-2015-18", "CC-MAIN-2015-22", "CC-MAIN-2015-27",
		"CC-MAIN-2015-32", "CC-MAIN-2015-35", "CC-MAIN-2015-40", "CC-MAIN-2015-48",
		"CC-MAIN-2016-07", "CC-MAIN-2016-18", "CC-MAIN-2016-22", "CC-MAIN-2016-26",
		"CC-MAIN-2016-30", "CC-MAIN-2016-36", "CC-MAIN-2016-40", "CC-MAIN-2016-44",
		"CC-MAIN-2016-50", "CC-MAIN-2017-04", "CC-MAIN-2017-09", "CC-MAIN-2017-13",
		"CC-MAIN-2017-17", "CC-MAIN-2017-22", "CC-MAIN-2017-26", "CC-MAIN-2017-30",
		"CC-MAIN-2017-34", "CC-MAIN-2017-39", "CC-MAIN-2017-43", "CC-MAIN-2017-47",
		"CC-MAIN-2017-51", "CC-MAIN-2018-05", "CC-MAIN-2018-09", "CC-MAIN-2018-13",
		"CC-MAIN-2018-17", "CC-MAIN-2018-22", "CC-MAIN-2018-26", "CC-MAIN-2018-30",
		"CC-MAIN-2018-34", "CC-MAIN-2018-39", "CC-MAIN-2018-43", "CC-MAIN-2018-47",
		"CC-MAIN-2018-51", "CC-MAIN-2019-04", "CC-MAIN-2019-09", "CC-MAIN-2019-13",
		"CC-MAIN-2019-18" ]
		 
#Choose random segment
random.shuffle(prefix_list)

cc.crawl_cc(prefix_list, write_bucket, workers = 16)

#cc.lid_cc(input_dir, "./Output", lid_model)