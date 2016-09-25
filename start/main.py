from constants import *
import sys
import os , os.path
from  generate import Generate
from recognize import Recognize


def main():
	if len(sys.argv) < 2:
		print "Invalid Argument"
		print "to train -> '--train'"
		print "to test -> '-t <testing_file_name>'"
		print "to remove add -> -rm <file_name>"
	elif sys.argv[1] == '--train':
	    f = "test.mp4"
	    text_file = "test.txt"
			        
        
		                
main()
        		



