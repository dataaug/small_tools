#读取文件中所有文件的路径

import sys
import os
import cv2
input_path = os.listdir('input')

for i in range(len(input_path) -1, -1, -1):
    if input_path[i][0] == '.':
        del input_path[i]
    else:
        input_path[i] = 'input/' + input_path[i]
for path in input_path:
    dress = cv2.imread(path)

print(dress.shape)



# python main.py --input 'input/input_2.png' 'input/input_3.png' 'input/input_4.png' 'input/input.png' --output output