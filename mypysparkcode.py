#accept a matrix as a input and find its tranpose
from numpy import*

r,c= [int(i) for i in input('how many rows, cols?').split(',')]
arr = zeros((r,c),dtype = int)
print('Enter matrix:')

for i in range(r):
    arr[i]=[int(x) for x in input().split()]

m= matrix(arr)
m1=m.transpose()
print('matrix is \n',m)
print('tranpose of matrix is\n',m1)

