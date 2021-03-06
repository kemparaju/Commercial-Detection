import os
import convertTime
from constants import *
import ffmpeg
from dejavu import Dejavu, decoder
from dejavu.recognize import FileRecognizer, DataRecognizer
import numpy as np
from tokenExtract import getDuration, DatabaseFile
import sys

class Recognize(object):

    def __init__(self, video_name):
        
        self.video_name = video_name
        self.djv = Dejavu(CONFIG)

        ffmpeg.createAudio(self.video_name, TEMP_AUDIO)
        self.frames, self.Fs, hash_val = decoder.read(TEMP_AUDIO)
        self.frames = self.frames[0] 
        self.duration = int(self.frames.shape[0] / (self.Fs*1.0))
        
    def findCommercial(self, start, span=5):
        
        data = np.copy(self.frames[start*self.Fs:(start+span)*self.Fs]) 
        song = self.djv.recognize(DataRecognizer , [data]) 
        if song is None:
            return [start, []] 
            
        if song["confidence"] >= 10:
            
            if song["offset_seconds"] < 0:
                return [start, []]
            
            start -= song["offset_seconds"]
            start = int(start)
            index = int(song["song_name"])
            
            name, duration = DatabaseFile("commercials.csv").getLine(index)
            
            if duration < song["offset_seconds"]:
                return [start, []]
            
            end = start + duration
                      
            return [end, [start, name]]
        else:
            return [start, []]
            
    def recognize(self):
        
        add_labels = getDuration(output_file="add_Names.txt") 
        un_file = getDuration(output_file="unclassifieds.txt")
        
        i = 0
        prev = 0
        while i < self.duration:
            remaining_time = self.duration - i
            sys.stdout.write('\r')
            sys.stdout.write("Pending analysis: %s" % convertTime.getStringTime(remaining_time))
            sys.stdout.flush()
            
            next, data = self.findCommercial(i)
                       
            if len(data) != 0:
                start = data[0]
                name = data[1]
                i = next + (VIDEO_GAP / 2)
                
                if (start - prev) >= VIDEO_SPAN:
                    un_file.writeLabels([convertTime.getStringTime(prev), convertTime.getStringTime(start), "not recognized"])
                    
                else:
                    start = prev 
                
                prev = next   
                
                add_labels.writeLabels([convertTime.getStringTime(start), convertTime.getStringTime(next), name])                     
            
            else:
                i += VIDEO_GAP
        print
                
        if (self.duration - prev) > 1: 
            un_file.writeLabels([convertTime.getStringTime(prev), convertTime.getStringTime(self.duration), "not recognized"])
        
 
            
      
                                    
    def __del__(self):
        
        os.remove(TEMP_AUDIO)
                
def foo(vid_name):
    
    recog = Recognize(vid_name)
    recog.recognize()
    
if __name__ == "__main__":
    foo(sys.argv[1])




