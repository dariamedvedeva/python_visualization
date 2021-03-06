# -*- coding: utf-8 -*-
# 3 columns: x, y and intencity
import sys
import os
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
global kpt

if len (sys.argv) > 1:
    print ("Ploting...".format (sys.argv[1]) )
    input_filename = sys.argv[1]
    kpt = int(sys.argv[2])
    print(kpt)
else:
    print ("Enter filename and number of kpoints.")



#save picture
def save(name = '', fmt = 'png'):
    pwd = os.getcwd()
    plt.savefig('%s.%s' % (name, fmt), fmt = 'png')
    os.chdir(pwd)


def picture():
    
    ##############
    # read file
    ##############
    f = open(input_filename)
    data = f.readlines()

    global kpt
    intensity = [ [0.0] * np.int(kpt) for i in range(np.int(kpt)) ]

    i=0
    j=0

    print(data.__len__())
    
    value = []
    
    for str in data:
        value.append( str.split() )
        
    print(value.__len__())
    
    while (i < kpt):
        while (j < kpt):
            intensity[i][j] = float(value[kpt * i + j][2])
            print (intensity[i][j])
            j += 1
        else:
            i += 1
        j = 0

    #############################
    # PLOT
    ############################
    plt.figure()
    plt.imshow(intensity, origin="lower", cmap=cm.rainbow)

    # plt.xticks((0, 49), ('$\Gamma$', 'K'), color='k', size=20)
    # plt.yticks((0, 49), ('$\Gamma$', 'K'), color='k', size=20)

    plt.grid(False)
    plt.axis('off')
    plt.colorbar()
    plt.draw()

    filename = 'out'
 #   save(name=filename, fmt='pdf')
 #   save(name=filename, fmt='png')
    print ("Finish.")
    plt.show()
    exit()

picture()
