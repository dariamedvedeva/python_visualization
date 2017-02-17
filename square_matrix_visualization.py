# for square matrix

# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

global filename
global kpt
global intensity

filename = ''
kpt = 0

#########################################
# input arguments:                      #
# filename and size of one dimention    #
# of matrix                             #
#########################################
if len (sys.argv) > 1:
    print ("Ploting...".format (sys.argv[1]) )
    filename = sys.argv[1]
    kpt = int(sys.argv[2])
    print(kpt)
else:
    print ("Enter filename")
    os.abort()


################
# save picture #
################
def save(name = '', fmt = 'png'):
    pwd = os.getcwd()
    plt.savefig('%s.%s' % (name, fmt), fmt = 'png')
    os.chdir(pwd)

#############
# read file #
#############
def read_file():
    global filename
    global kpt
    global intensity
    f = open(filename)
    data = f.readlines()
    
    intensity = [ [0.0] * np.int(kpt) for i in range(np.int(kpt))]

    i = 0
    j = 0
    for str in data:
        value = str.split()
        value = [float(x) for x in value]
        intensity[i][j] = value[2]
        i +=1
        if(i==kpt):
            j += 1
            i  = 0
    f.close()

######################
# plot square matrix #
######################
def picture():
    global intensity, kpt, filename
    plt.figure()
    # plt.title('Static magnetic susceptibility X(q)\n', color='k', size=20)

    size_mesh = kpt * kpt
    X = [[0.0] for i in range(np.int(kpt*kpt))]
    Y = [[0.0] for i in range(np.int(kpt*kpt))]

    for i in range(kpt):
        X[i] = i
        Y[i] = X[i]


    plt.imshow(intensity, origin="lower", cmap=cm.rainbow)

    # plt.xticks((0, 49), ('$\Gamma$', 'K'), color='k', size=20)
    # plt.yticks((0, 49), ('$\Gamma$', 'K'), color='k', size=20)

    plt.grid(True)
    plt.axis('on')
    plt.colorbar()
    plt.draw()


 #   save(name=filename, fmt='pdf')
    save(name=filename, fmt='png')

#    plt.show()
    exit()

#############
# execution #
#############
read_file()
picture()
