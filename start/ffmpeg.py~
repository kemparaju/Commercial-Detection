"""used for chopping each Training Samples from
   given Test data
 """

import os

def createVideo(start , duration , vid_src , vid_dst , force_fps=False , fps = 60):
    print "Creating video @"+vid_dst
    os.system("ffmpeg -ss "+start+" -i "+vid_src+" -t "+duration+" -acodec copy -vcodec copy "+vid_dst+" -loglevel quiet" )
    if force_fps:
        os.system("ffmpeg -ss " + video_dst + " -vf fps=1/" + str(fps) + " " + video_dst)
    print "Done"


def createAudio(vid_src , aud_dst , rate=44100 , channels=1 , block="160k"):
    print "Creating audio for"+vid_src

    os.system("ffmpeg -i "+vid_src+" -ab "+block+" -ac "+str(channels)+" -ar "+str(rate)+" -vn "+aud_dst+" -loglevel quiet")
    print "Done"

