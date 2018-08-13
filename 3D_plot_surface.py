import subprocess
import numpy as np
import sys
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

print "arguments: 1) script name 2) file path 3) X axis 4) Y axis 5) Z axis"

if len (sys.argv) > 1:
    filepath  = sys.argv[1]
    x_column  = int(sys.argv[2])
    y_column  = int(sys.argv[3])
    z_column  = int(sys.argv[4])
else:
    print ("Check arguments according to the list")


def read_file(filename):
    # structure of file : bosonic_freq fermionic_freq fermionic_freq Re_part Im_part
    # z should be square to be plotted
    f   = open(filename, "r")
    lines = f.readlines()
    
    size = int(np.sqrt(len(lines)))
    x = np.zeros(size, dtype=np.float)
    y = np.zeros(size, dtype=np.float)
    values = np.zeros(size**2, dtype=np.float)
    z = np.zeros((size, size), dtype=np.float)
    
    i = 0
    for line in lines:
        params = line.split()
        if (i < size):
            x[i] = float(params[y_column])
            y[i] = float(params[y_column])

        values[i] = float(params[z_column])
        i = i + 1
    
    print "min value = ", min(values)
    print "max value = ", max(values)
    
    for m in range(size):
        for n in range(size):
            z[m][n] = values[n + size * m]

    f.close()

    return x, y, z

# Read file
x, y, Z = read_file(filepath)

# Plot
fig = plt.figure()
ax = plt.axes(projection='3d')
X, Y = np.meshgrid(x, y)

# 1. black-whyte contour
#ax.contour3D(X, Y, Z, 50, cmap='binary')

# 2. colored surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
plt.show()
