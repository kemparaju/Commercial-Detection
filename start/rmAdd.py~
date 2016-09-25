import ffmpeg
from constants import *
from tokenExtract import getDuration
from convertTime import getDiffTime
import os
import sys
def removeAdd(vid_name , file_name , vid_ext=".mp4"):
    labels = getDuration(file_name)
    
    data = labels.readLabels()
    fname=1;
    
    f = open("concat_list.txt" ,"w")
    
    for i in data:
        start = i[0]
        end = i[1]        
        duration = getDiffTime(start , end)
        
        ffmpeg.createVideo(start,duration,vid_name,UN_VIDEO+str(fname)+vid_ext)
        
        line = "file \'"+UN_VIDEO+str(fname)+vid_ext+"\'\n"
        f.write(line)
        fname +=1
    line = "ffmpeg -f concat -i concat_list.txt -c copy "+OUT_DIR+vid_name
    print "ffmpeg -f concat -i concat_list.txt -c copy ../output/s2.mp4"
    print line
    
    os.system(line)

		
		
def foo(vid_name , file_name):
    removeAdd(vid_name , file_name)
    

if __name__ == "__main__":
    foo(sys.argv[1] , sys.argv[2])


			
        
