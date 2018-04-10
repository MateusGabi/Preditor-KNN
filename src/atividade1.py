import matplotlib.pyplot as plt
import csv

wd = csv.reader(open('data/alturapeso.csv'))

mX = []
mY = []
fX = []
fY = []
for line in wd:
    if int(line[2]) == 0:
        mX.append(float(line[0]))
        mY.append(float(line[1]))
    else:
        fX.append(float(line[0]))
        fY.append(float(line[1]))        

plt.plot(mX, mY, 'ro', color='b', label='Masculino')
plt.plot(fX, fY, 'ro', color='r', label='Feminino')

plt.xlabel('Altura')
plt.ylabel('Peso')

plt.legend()
plt.show()
