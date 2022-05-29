import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Symbol,limit

x = Symbol('x')
y=(8**x-4**x)/(4*x)

limit(y,x,0)
print(limit(y,x,0))

plt.grid()
X=np.linspace(-3,3,100)

def f(X):
	return (8**X-4**X)/(4*X)

plt.plot(X,f(X))

A=[0]
B=[limit(y,x,0)]
plt.plot(A,B,'o')
for xy in zip(A,B):
	plt.annotate('(%s, %s)'%xy,xy=xy,xytext=(-60,10),textcoords='offset points')

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()

#we can see that the point is on the curve.so our answer is correct