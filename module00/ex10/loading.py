from sys import stdout
from time import sleep
from tqdm import tqdm
import time 

def ft_progress(listy):
    t1 = time.time()
    time_s = 0
    dlt = 0
    t2 = 0
    tm = 0
    for i in listy:
        if i == 1:
            t2 = time.time()
            dlt = t2-t1
            tm = dlt * len(listy)
        time_s = time_s + dlt
        stdout.write('\r')
        stdout.write("ETA: %.2fs" % (tm))
        stdout.write("[%3d%%]" % (((i+1) * 100)/len(listy)))
        stdout.write("[%s%s%s]" % ("="*(int)((i * 20)/len(listy)),'>'," "*(20 - (int)((i * 20)/len(listy)))))
        stdout.write("%d%s%d"%(i + 1, "/", len(listy)))
        stdout.write("| elapsed time %.2fs" % (time_s))
        stdout.flush()
        yield i

# Flag = True
Flag = False

if Flag == True:
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
else:
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.005)
    print()
    print(ret)