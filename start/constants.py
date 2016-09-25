
CONFIG = {
    "database": {
        "host" : "127.0.0.1" ,
        "user" : "root" ,
        "passwd" : "kemp1112",
        "db" : "fprint"
    }
}

CONFIDENCE_THRESH = 10


AUDIO_EXT = ".wav"
VIDEO_EXT = ".mp4"
DB_VIDEO = "./samples/video/"
DB_AUDIO = "./samples/audio/"
UN_VIDEO = "./temp/video/" 
DBNAME = "commercials.csv"
OUT_DIR = "../output/"

OUTPUT = "output.txt"

#in seconds
VIDEO_SPAN = 5 #How much to take to analyze audio
VIDEO_GAP = 15 #How much to skip
TEMP_VIDEO = "../testData/temp.mp4"
TEMP_AUDIO = "../testData/temp.wav"

#For fileHandler
UNCLASSIFIED_CONTENT = "unclassified"
