import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


number_of_block = 21

bath = 'B'

N_exc = 7
N_hol = 7

#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
file_name_ground_state_N_pls_1     =  "eigval" + str(number_of_block) + "part_decomp.dat"

num_of_spinorbit = 10

f = open(file_name_ground_state_N_pls_1, "r")
file_lines  = f.readlines()
ind         = 0
array       = []
for i in file_lines:
    if (ind == 1):
        line_data = i.split()
        for j in range(num_of_spinorbit):
            array.append(float(line_data[-10 + j]))
    ind += 1
print(array)
f.close


x = np.arange(1, num_of_spinorbit + 1, 1)
y = array

plt.title('N_exc = ' + str(N_exc) + ', N_hol = ' + str(N_hol) )

fig, ax = plt.subplots()
#ax.yaxis.set_major_formatter(formatter)
xl = plt.xlabel('Spin-orbitals (down, up)')
yl = plt.ylabel('Contribution')
plt.bar(x, y, facecolor='g')
plt.xticks(x)
plt.savefig('bath_' + bath + '_exc_' + str(N_exc) + '_hol_' + str(N_hol) + '_contr_sec' + str(number_of_block) + '.pdf')
plt.show()
