import os
import convertTime
from constants import *

class getDuration(object):

    def __init__(self , input_file=None , output_file=None):
        self.fname = input_file
        self.nfile = output_file
        self.wcount = 0


    def readLabels(self):
        with open(self.fname) as fd:
            for line in fd:
                if len(line) == 0:
                    break
                line = [line.strip() for line in line.split("=")]
                time = [i.strip() for i in line[0].split('-')]

                name = line[-1].strip()

                yield [time[0] , time[1] , name]
    def writeLabels(self , contents):
    
        if self.wcount == 0:
            f = open(self.nfile, 'w')
        else:
            f = open(self.nfile, 'a')
        
        start = contents[0]
        end = contents[1]
        name = contents[2]
        line = ""
        if type(start) == type(end) == int:
            line = convertTime.getStringTime(start) + " - " + convertTime.getStringTime(end) + " = " + name
        elif type(start) == type(end) == str:
            line = start + " - " + end + " = " + name
        line += '\n'
        f.write(line)
        f.close()
        self.wcount += 1
       
        
class DatabaseFile(object):
    
    """
        Used to handle operations on the database csv file
    """
    
    def __init__(self, filename):
    
        self.filename = filename
       
    def getLine(self, index):
        
        """
            Function gets the line in the database file based on the index.
            The index is acting as the line number in the database file.
            Returns: [name(string), duration(int)] 
        """
        
        f = open(self.filename)
        i = 1
        lines = f.readlines()
        for line in lines[1:]:
            if i == index:
                line = line.split(",")
                name = line[0]
                duration = line[1]
                duration = convertTime.getSecTime(duration)
                return [name, duration]
            i += 1
        print index, i
        print "Db and csv are not in sync"
        return -1

                
