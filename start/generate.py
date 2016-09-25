from tokenExtract import getDuration
from dejavu import Dejavu
from  constants  import *
from convertTime import *
import ffmpeg
import os
from rmAdd import removeAdd
import sys

class Generate(object):
	
	def __init__(self , video_name , label_name):
		self.video_name = video_name
		self.labelEntry = getDuration(label_name)
		self.add_names = []
		self.db = Dejavu(CONFIG)
        
        
		

	def createData(self , aud_ext , vid_ext):
		"""segment the data present in given training sample by using
			associated labels file
		 """
		label_data = self.labelEntry.readLabels()
		
		fname  = len(os.listdir(DB_AUDIO)) + 1
		
		try:
		    with open(DBNAME) as f:
		        lines = f.readlines()
		        self.add_names = [line.split(',')[0] for line in lines[1:]]
		    f = open(DBNAME , "a")    
			
		
		except:
		    print "creating csv file"		    
		    f = open(DBNAME , "w")
		    f.write("NAME , DURATION , PATH\n")    
            		           

		for data in label_data:
			start = data[0]
			end = data[1]
			name = data[2]
			
			if self.add_names != [] and (name in self.add_names):
			    print "Fingerprint for "+name+" is already present"
			    continue
                
                

			duration = getDiffTime(start , end)
			ffmpeg.createVideo(start,duration,self.video_name,DB_VIDEO+str(fname)+vid_ext)
			ffmpeg.createAudio(DB_VIDEO+str(fname)+vid_ext , DB_AUDIO+str(fname)+aud_ext)
			
			
			temp = ",".join([name , duration])
			temp = temp+","+str(fname)+vid_ext+"\n"
			f.write(temp)
			fname += 1
       


	def fingerPrintData(self ,aud_ext ):
	    self.db.fingerprint_directory(DB_AUDIO , [aud_ext])
		

	def run(self , aud_ext=".wav" , vid_ext=".mp4"):
	    self.createData(aud_ext , vid_ext)
	    print "Extraction done!!"
	    wait = raw_input("Starting fingerprinting...")
	    self.fingerPrintData(aud_ext)
	    
		
		
def foo(vid_name , label_name):
    gen = Generate(vid_name , label_name)
    gen.run()		

if __name__ == "__main__":
    foo(sys.argv[1] , sys.argv[2])






    
