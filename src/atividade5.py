import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def convert2array(imgr):
    d = []
    for l in imgr:
        for c in l:
            d.append((255 - c[0]))
    return d



class Digitos:
    def __init__(self,img):
        self.drawing = False # true if mouse is pressed
        self.ix,iy = -1,-1
        self.count = 0
        self.xtrain = []
        self.ytrain = []
        self.training = True
        self.neigh = KNeighborsClassifier(n_neighbors=3)
        self.drawing = False
        self.img = img



    def save_dataset(self):
        f = open('data/dataset.csv','a')
        x = self.xtrain
        y = self.ytrain
        for i in range(len(x)):
            line = ','.join(str(v) for v in x[i]) +','+str(y[i])+'\n'
            f.write(line)
        f.close()

    def load_dataset(self):
        f=open('data/dataset.csv')
        xtrain = []
        ytrain = []
        nlines = 0
        for line in f:
            nlines += 1
            v = [int(x) for x in line.rstrip('\n').split(',')]
            xtrain.append(v[:-1])
            ytrain.append(v[-1])
        print "Loaded %d lines\n"%(nlines)
        for i in  set(ytrain):
            print "class %d count %d"%(i,ytrain.count(i))
        self.xtrain = xtrain
        self.ytrain = ytrain

    def train(self):   
        self.neigh.fit(self.xtrain, self.ytrain)
        
        #Test com tamanho de 25
        x_train, x_test, y_train, y_test = train_test_split(self.xtrain, self.ytrain, test_size=0.25, random_state=42)


        # COLOQUE AQUI O CODIGO PARA TREINAMENTO DO ALGORITMO
    def draw_circle(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix,self.iy = x,y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                 cv2.circle(self.img,(x,y),5,(0,0,0),-1)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.circle(self.img,(x,y),5,(0,0,0),-1)
            if self.training: 
                imgr = cv2.resize(self.img,(8,8),interpolation=cv2.INTER_AREA)
                self.img.fill(255)
                self.xtrain.append(convert2array(imgr))
                self.ytrain.append(self.count)
                imgr = cv2.resize(imgr,(128,128))
                self.count = (self.count+1)%3
                print "Draw the number %d\n"%(self.count)
                cv2.imshow('result',imgr)
            else:
                imgr = cv2.resize(self.img,(8,8),interpolation=cv2.INTER_AREA)
                instance = np.matrix(convert2array(imgr)).reshape(1,-1)
                imgr = cv2.resize(imgr,(128,128))
                cv2.imshow('result',imgr)
                # a instancia esta pronto em instance. utilize o predict em instance para predizer o novo exemplo
                self.img.fill(255)
                print self.neigh.predict(instance)


if __name__=='__main__':
    img = np.zeros((128,128,3), np.uint8)
    img.fill(255)
    obj = Digitos(img)
    cv2.namedWindow('image')
    cv2.namedWindow('result')
    cv2.setMouseCallback('image',obj.draw_circle)
    print "Draw the number 0\n"
    while(1):
        cv2.imshow('image',obj.img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        elif k == ord('m'):
            obj.training = not obj.training
            if obj.training:
                print "Training mode"
                print "Draw the number %d"%(obj.count)
            else:
                print "Classify mode"
        elif k == ord('s'):
            obj.save_dataset()
            print "Dataset saved!"
        elif k == ord('t'):
            obj.train()
            print "Classifier trained!"
        elif k == ord('l'):
            obj.load_dataset()
            print "Dataset loaded!"
        elif k == ord('c'):
            obj.xtrain = []
            obj.ytrain = []
            obj.count = 0
            print "Dataset cleared"


            



cv2.destroyAllWindows()
