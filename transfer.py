#将图片转换为固定大小并且保持比例
import cv2
item = 'input.jpeg'
dress = cv2.imread(item)
dress = cv2.imread(dress)
width = dress.shape[1]
height = dress.shape[0]

max = width if width >= height else height
pad_height = int((max - height)/2)
pad_width = int((max - width)/2)
dress = cv2.copyMakeBorder(dress,pad_height, pad_height, pad_width, pad_width,cv2.BORDER_CONSTANT,value = 1)
dress = cv2.resize(dress,(512,512), interpolation = cv2.INTER_AREA)
item = dress

cv2.imwrite('./input.png',dress)

