import time

def write_log (text,user):
    log = open("botlog.txt", "a")
    log.write(str(time.ctime())+"/"+str(user)+": "+str(text)+"\n")
    log.flush()
    return
