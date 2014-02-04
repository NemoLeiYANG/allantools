

# this files runs all the tests defined in the subdirectories

import time
import sys
sys.path.append("..") # allows importing allantools from parent dir


from nbs14 import nbs14_test
from phase.dat import phase_dat_test

if __name__ == "__main__":
	
	start = time.clock()
	
	nbs14_test.run()
	phase_dat_test.run()
	
	end = time.clock()
	print "Tests done in %2.3f s" % (end-start)