# Mededeva 11.11.2019

import matplotlib.pyplot as plt

file_name_ground_state_N_mns_1   = "B/eigval18part.dat"
file_name_ground_state           = "B/eigval19part.dat"
file_name_ground_state_N_pls_1   = "B/eigval20part.dat"

#### Central block N
number_of_central_block = 19
num_of_eigval           = 90
eigval_central_block    = []
f = open(file_name_ground_state, "r")
file_lines = f.readlines()
for i in file_lines:
    line_data = i.split()
    eigval_central_block.append(float(line_data[0]))
    
x_central = [number_of_central_block] * num_of_eigval
y_central = eigval_central_block
f.close


#### N - 1 block
number_of_left_block    = number_of_central_block - 1
eigval_left_block       = []
f = open(file_name_ground_state_N_mns_1, "r")
file_lines = f.readlines()
for i in file_lines:
    line_data = i.split()
    eigval_left_block.append(float(line_data[0]))
    
x_left = [number_of_left_block] * num_of_eigval
y_left = eigval_left_block
f.close

#### N + 1 block
number_of_right_block    = number_of_central_block + 1
eigval_right_block       = []
f = open(file_name_ground_state_N_pls_1, "r")
file_lines = f.readlines()
for i in file_lines:
    line_data = i.split()
    eigval_right_block.append(float(line_data[0]))
    
x_right = [number_of_right_block] * num_of_eigval
y_right = eigval_right_block
f.close


##### Plot
x = [number_of_left_block, number_of_central_block, number_of_right_block]

labels = [str(int(number_of_left_block)), str(int(number_of_central_block)), str(int(number_of_right_block))]

plt.plot(x_central, y_central, '.',  x_left, y_left, '.', x_right, y_right, '.')


# To write values of lower energy
#
# txt = plt.text(x, y, 'text')
txt = plt.text(number_of_central_block - 0.2, y_central[0] - 0.07 , round(y_central[0], 4))

txt = plt.text(number_of_left_block - 0.2, y_left[0] - 0.07 , round(y_left[0], 4))

txt = plt.text(number_of_right_block - 0.2, y_right[0] - 0.07 , round(y_right[0], 4))


# dif
# position of numbers
if (y_left[0] < y_right[0]) :
    position = y_right[0]
else:
    position = y_left[0]
     
# dif left and central
dif_left_center = (number_of_central_block + number_of_left_block) / 2.
txt = plt.text(dif_left_center, position, 'dif = \n' +
str(round(y_central[0] - y_left[0], 4)))

# dif right and central
dif_right_center = (number_of_central_block + number_of_right_block) / 2.
txt = plt.text(dif_right_center, position, 'dif = \n' +
str(round(y_central[0] - y_right[0], 4)))

xl = plt.xlabel('Number of particles')
yl = plt.ylabel('Energy')

plt.xticks(x, labels, rotation='horizontal')
plt.margins(0.1)
plt.subplots_adjust(bottom=0.15)
plt.show()
