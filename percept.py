import numpy as np

class percept():

    def __init__(self, inputney, layouts, outputney, countLearn ):
        np.random.seed(1)
        self.syn = []
        self.l   = []
        self.countLearn = countLearn
        self.layouts = layouts
        for i in range(layouts+2):
            self.l.append([])
            if i < layouts +1:
                self.syn.append([])
        for i in range(layouts+1):
            if i == 0:
                self.syn[i] = 2*np.random.random((inputney,layouts)) - 1
            elif i == layouts:
                self.syn[i] = 2*np.random.random((layouts*layouts, outputney)) - 1
            else:
                self.syn[i] = 2*np.random.random((layouts*i,layouts*(i+1))) - 1

    def nonlin(self,x,deriv=False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))

    def learn(self, x, y, check=False, count=1000):
        for j in xrange(self.countLearn):
            l_error = []
            l_delta = []
            for i in range(0,self.layouts+2):
                l_error.append([])
                l_delta.append([])
            self.getRes(x)
            i = self.layouts+1
            while(i>=1):
                if i == self.layouts+1:
                    l_error[i] = y - self.l[i]

                    if (j% count) == 0 and check:
                        print "Error"+str(j)+":" + str(np.mean(np.abs(l_error[i])))

                    l_delta[i] = l_error[i]*self.nonlin(self.l[i],deriv=True)
                else:
                    l_error[i] = l_delta[i+1].dot(self.syn[i].T)
                    l_delta[i] = l_error[i]*self.nonlin(self.l[i],deriv=True)
                i = i - 1
            i = self.layouts
            while(i>=0):
                self.syn[i] += self.l[i].T.dot(l_delta[i+1])
                i = i - 1

    def getRes(self, x):
        for i in range(self.layouts+2):
            if i == 0:
                self.l[i] = x
            elif i == self.layouts+1:
                self.l[i] = self.nonlin(np.dot(self.l[i-1],self.syn[i-1]))
                return self.l[i]
            else:
                self.l[i] = self.nonlin(np.dot(self.l[i-1],self.syn[i-1]))

    def save(self,file):
        f = open(file,"w")
        for i in self.syn:
            for j in i:
                for z in list(j):
                    f.write(str(z)+" ")
                f.write("\t")
            f.write("\n")
        f.close()

    def load(self,file):
        f = open(file,"r")
        z = 0
        l = [line.split("\n") for line in f]
        for i in l:
            f = []
            for j in i[0].split("\t"):
                if j == '':
                    continue
                g = []
                for d in j.split():
                    g.append(float(d))
                f.append(g)
            self.syn[z] = np.array(f)
            z = z +1

if __name__ == "__main__":
    nt = percept(255,9,255,1000000)

    X = np.array([
        ])
    y = np.array([
        ])

    text = 'hello'
    tmpx = []
    for i in range(255):
        if i < len(text):
            tmpx.append(ord(text[i]))
        else:
            tmpx.append(0)
    texta= 'hello, how are you?'
    tmpy = []
    for i in range(255):
        if i < len(texta):
            tmpy.append(ord(texta[i]))
        else:
            tmpy.append(0)
    tmp = X.tolist()
    tmp.append(tmpx)
    X = np.array(tmp)
    tmp = y.tolist()
    tmp.append(tmpy)
    y = np.array(tmp)

    text = 'bye'
    tmpx = []
    for i in range(255):
        if i < len(text):
           tmpx.append(ord(text[i]))
        else:
            tmpx.append(0)
    texta= 'Okey );'
    tmpy = []
    for i in range(255):
        if i < len(texta):
            tmpy.append(ord(texta[i]))
        else:
            tmpy.append(0)
    tmp = X.tolist()
    tmp.append(tmpx)
    X = np.array(tmp)
    tmp = y.tolist()
    tmp.append(tmpy)
    y = np.array(tmp)

    X = X * 0.0001
    y = y * 0.0001
    #print X
    #nt.load("231s3.txt")
    nt.learn(X,y,True,10000)
    print 'Learning ended'
    nt.save("231s3.txt")
    print 'Saving ended'
    tmp = raw_input()
    tmpx = []
    for i in range(255):
        #print i < len(tmp)
        if i < len(tmp):
            tmpx.append(ord(tmp[i]))
        else:
            tmpx.append(0)
    #print tmpx
    x = np.array([
            tmpx
        ])
    res = (nt.getRes(x)*10000).tolist()[0]
    #print res
    textend = ''
    for i in res:
        if i>255:
            continue
        textend += chr(int(round(i)))
    print textend
