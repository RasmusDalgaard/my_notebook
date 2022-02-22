import numpy as np

matrix = np.arange(10,30).reshape(4,5)

yellow = matrix[0,0]
cyan = matrix[:,1]
red = matrix[0, 1:4]
green = matrix[0:3,2]
blue = matrix[:2, 4]

print('red:',red,'\n blue:',blue,'\n green:\n',green,'\n cyan:',cyan, '\n yellow:',yellow)

cube = np.arange(0,27).reshape((3,3,3))

a = cube[1, 1, :]
b = cube[:, 1, 0]
c = cube[0,:,2]

print('\n a:',a, '\n b:',b, '\n c:',c)

