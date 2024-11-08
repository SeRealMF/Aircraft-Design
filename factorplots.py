import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def getfactor(airplanelistcsv,value,Rphys):
    data = pd.read_csv(airplanelistcsv)  # csv Datei einlesen
    x = np.array(data['RB'])
    y = np.array(data[value])
    fittedfactor = np.polyfit(x, y, 2)
    p = np.poly1d(fittedfactor)
    calculated=p(Rphys)
    return (calculated)


def plotfactor(airplanelistcsv,value):
    data = pd.read_csv(airplanelistcsv)  # csv Datei einlesen
    x = np.array(data['RB'])
    y = np.array(data[value])
    fittedFuelFactor = np.polyfit(x, y, 2)
    p = np.poly1d(fittedFuelFactor)
    xp = np.linspace(min(x),max(x),100)
    plt.plot(xp,p(xp),'-')
    plt.scatter(x,y, color='#aaaaaa')
    plt.xlabel('Range [km]')
    plt.ylabel(value)
    #plt.title(name)
    plt.show()

def rangepayloadplot(Rphys,mPayload,RphysC,mPayloadC):
    A = ['A',0,mPayload]
    B = ['B',Rphys,mPayload]
    C = ['C',RphysC,mPayloadC]
    D = ['D',RphysC,0]
    data = [A,B,C,D]
    plotdata = [[],[]]
    for i in data:
        plotdata[0].append(i[1])
        plotdata[1].append(i[2])
        plt.annotate(i[0], (i[1], i[2]))
    plt.plot(plotdata[0], plotdata[1], '-',color='#ff0000')
    plt.scatter(plotdata[0], plotdata[1], color='#aaaaaa')

    plt.xlabel('Range [km]')
    plt.ylabel('Payload [kg]')
    plt.show()


rangepayloadplot(5000,5000,7000,3000)



#print(getfactor('airplane_list.csv','Payload factor',100))
#plotfactor('airplane_list.csv','Fuel factor')

