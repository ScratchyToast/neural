import percept as pt
import wordtovec as wd
import threading as threads
import numpy as np

def ntstart(nt, x, y, text):
    nt.learn(x,y,True,10000)
    print(wd.arrNumToWord((nt.getRes(wd.wordToNum(textx1))*10000).tolist()))

nt  = pt.percept(255,10,255,70000)
nt2 = pt.percept(255,10,255,70000)

textx1 = 'hello'
texty1 = 'hello, idiot'

X1 = np.array([ wd.wordToNum(textx1) ]) * 0.0001
y1 = np.array([ wd.wordToNum(texty1) ]) * 0.0001

textx2 = 'bey'
texty2 = 'bey, idiot'

X2 = np.array([ wd.wordToNum(textx2) ]) * 0.0001
y2 = np.array([ wd.wordToNum(texty2) ]) * 0.0001

threads.Thread(target=ntstart,     args=(nt,X1,y1,textx2)).start()
threads.Thread(target=ntstart,     args=(nt2,X2,y2,textx1)).start()
