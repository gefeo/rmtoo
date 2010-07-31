#
# Blackbox rmtoo tests
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import clear_result_is, compare_results

mdir = "tests/blackbox-test/bb002-test"

class TestBB001:

    def test_pos_001(self):
        "BB Basic with one requirement - reqs only from FILES"

        clear_result_is(mdir)
        main(["-f", mdir + "/input/Config2.py", "-m", ".."])
        missing_files, additional_files, diffs = compare_results(mdir)
        assert(len(missing_files)==0)
        assert(len(additional_files)==0)
        # The count stats is always different because of the timestamp
        print("DIFFS: %s" % diffs)
        assert(len(diffs)==0)
        # Diffs are the from the stats count file:
        # ['---  \n', 
        #  '+++  \n', 
        #  '@@ -1,1 +1,5 @@\n', 
        #  '-2010-07-31_06:11:27 1\n', -- or similar
        #  '+2010-07-30_21:04:35 1\n', 
        #  '+2010-07-30_21:03:22 1\n',
        #  '+2010-07-30_20:57:36 1\n',
        #  '+2010-07-29_21:17:15 1\n',
        #  '+2010-07-29_21:09:03 1\n']
        #assert(len(diffs["stats_reqs_cnt.csv"])==9)