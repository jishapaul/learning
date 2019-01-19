>>> import numpy as np
>>> mylist = [1,2,3]
>>> x = np.array(mylist)
>>> print (x)
[1 2 3]
>>> y = np.array([4,5,6])
>>>
>>> m = np.array([[7,8,9],[10,11,12]])
>>>
>>> print (m)
[[ 7  8  9]
 [10 11 12]]
>>> m.shape
(2, 3)
>>> n=np.arange(0,30,2)
>>> print (n)
[ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28]
>>> n.shape
(15,)

>>> print (n)
[[ 0  2  4  6  8]
 [10 12 14 16 18]
 [20 22 24 26 28]]
>>> o = np.linspace(0,4,9)
>>>
>>> print (o)
[ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4. ]
>>> o.resize(3,3)
>>>
>>> print (o)
[[ 0.   0.5  1. ]
 [ 1.5  2.   2.5]
 [ 3.   3.5  4. ]]
>>> np.ones((3,2))
array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])

>>> np.zeros((3,2))
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])
>>> np.eye(3)
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
>>> np.diag(y)
array([[4, 0, 0],
       [0, 5, 0],
       [0, 0, 6]])
>>> print(y)
[4 5 6]
>>> np.array([1,2,3]*3)
array([1, 2, 3, 1, 2, 3, 1, 2, 3])
>>> np.repeat([1,2,3],3)
array([1, 1, 1, 2, 2, 2, 3, 3, 3])
>>>
>>> p = np.ones([2, 3], int)
>>> print (p)
[[1 1 1]
 [1 1 1]]
>>> np.vstack([p, 2*p])
array([[1, 1, 1],
       [1, 1, 1],
       [2, 2, 2],
       [2, 2, 2]])
>>> np.vstack([p, 4*p])
array([[1, 1, 1],
       [1, 1, 1],
       [4, 4, 4],
       [4, 4, 4]])
>>> np.hstack([p, 4*p])
array([[1, 1, 1, 4, 4, 4],
       [1, 1, 1, 4, 4, 4]])
>>> print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
[5 7 9]
>>> print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]
[-3 -3 -3]
>>> print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
[ 4 10 18]
>>> print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]
[ 0.25  0.4   0.5 ]
>>> print (x**2)
[1 4 9]
>>> x.dot(y)
32
>>> z = np.array([y, y**2])
>>> print (z)
[[ 4  5  6]
 [16 25 36]]
>>>
>>>
>>> z.shape
(2, 3)
>>> z.T
array([[ 4, 16],
       [ 5, 25],
       [ 6, 36]])
>>> z.T.shape
(3, 2)
>>> z.dtype
dtype('int32')
>>> z= z.astype('f')
>>> z.dtype
dtype('float32')
>>> print (z)
[[  4.   5.   6.]
 [ 16.  25.  36.]]
>>> a = np.array([-4, -2, 1, 3, 5])
>>>
>>> a.sum()
3
>>> a.mean()
0.59999999999999998
>>> a.std()
3.2619012860600183
>>> a.argmax()
4
>>> a.argmin()
0
>>>

