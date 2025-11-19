from typing import List
from Kernel import Kernel, init

def applyKernel(line, column, kernel, image):
    s = 0
    for lin in range(len(kernel)):
        for col in range(len(kernel[0])):
            s += image[line + lin][column + col] * kernel[lin][col]

    sk = sum([sum(k) for k in kernel])
    if sk <= 0:
        sk = 1
    s = s / sk

    if ( s > 255):
        s = 255

    if ( s < 0):
        s = 0

    return s

# print(f"Todos {kernel}\n")
# print(f"Posição {kernel[0][1]}\n")

def getGrayLevel(i,j, kernel, image):
    line = i - 1
    column = j - 1
    return applyKernel(line, column, kernel,image)

def filter_function(image: List[List[int]], kernel: List[List[int]]):

    stride = (1,1)
    filtered = image[:]

    for i in range(len(image)):
        for j in range(len(image[i])):
            # borda fica 0
            if (i == 0 or j == 0 or 
                i == len(image)-1 or 
                j == len(image[i])-1):
                filtered[i][j] = 0
            else:
                filtered[i][j] = getGrayLevel(i, j, kernel, image)

           
    return filtered

Kernel = Kernel("minion.png", filter_function)

init()