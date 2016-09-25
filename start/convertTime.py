def getStringTime(sec_time):

    hr_sec = 3600
    min_sec = 60

    hr = sec_time/hr_sec

    sec_time -= hr*hr_sec

    mn = sec_time/min_sec

    sec_time -= mn*min_sec

    sc = sec_time
    
    if(mn<10):
        mn = "0"+str(mn)
    if(hr<10):
        hr = "0"+str(hr)
    if(sc<10):
        sc = "0"+str(sc)

    str_time =  str(hr)+":"+str(mn)+":"+str(sc)
    return str_time

def getSecTime(str_time):
    time = [int(i.strip()) for i in str_time.split(":")]
    n = len(time)
    sec_time = 0

    for i in range(n):
        sec_time = sec_time+time[i] * (60**(n-1-i))

    return sec_time

def getDiffTime(str1 , str2):
    sec_time1 = getSecTime(str1)
    sec_time2 = getSecTime(str2)
    if sec_time1 > sec_time2:
        print "time difference error"
        
    else:
        return getStringTime(sec_time2 - sec_time1)  
      
def test():
    time = getStringTime(36000)
    print time 

#test()
    

    
