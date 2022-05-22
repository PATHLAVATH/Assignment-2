import numpy as np

#creating matrix
A = np.matrix('[2,4; 3,5]')

#finding transpose of A
tA = A.T

#adding A and tA
R = A+tA

#finding tR
tR = R.T

#to check R is symmetric
if np.array_equal(R,tR):
    print("the matrix is symmetric")
else:
    print("the matrix is not symmetric")
    

