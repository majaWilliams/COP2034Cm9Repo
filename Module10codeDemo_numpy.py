# WilliamsMaja_08-01-2026
# Here is a comment visually expressing that I have read
# the directions correctly on the project page [mod 9].

#!usr/bin/env python3
#Module10codeDemo_numpy.py

import numpy as np
#print(np.__version__)

#Slide 7 Creating ndarrays from Lists
# integer array:
##npa = np.array([1, 4, 2, 5, 3])
##print(npa)

# upcast integers to float
##npa = np.array([3.14, 4, 2, 3])
##print(npa)

### specify array element type
##npa = np.array([1, 2, 3, 4], dtype='float32')
##print(npa)

### multidimensional array using list of lists
##npa = np.array([range(i, i + 3) for i in [2, 4, 6]])
##print(npa)

###Slide 8 Creating Arrays from Scratch
### create a 10-integer array filled with zeros
##npa = np.zeros(20, dtype=int)
##print(npa)
##
### create a 3x5 floating point array filled with ones
##npa = np.ones((3,5), dtype=float)
##print(npa)

### create a 3x5 array filled with 3.14
##npa = np.full((3,5), 3.14)
##print(npa)
##
### create an array filled with a linear sequence
### starting at 0, ending at 20, stepping by 2
### (similar to built-in range() function)
##npa = np.arange(2, 25, 3)
##print(npa)

###Slide 9 Creating Arrays from Scratch
### create a 3x3 array of uniformly distributed
### random values between 0 and 1
##npa = np.random.random((3,3))
##print(npa)

### create a 3x3 array of normally distributed random
### values with mean 0 and standard deviation 1
##npa = np.random.normal(0,1,(3,3))
##print(npa)

###Slide 13 NumPy Array Attributes
np.random.seed(0) # seed random generator
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))
##
##print("x1: ")
##print(x1)
##
##print("x1 ndim: ", x1.ndim)
##print("x1 shape: ", x1.shape)
##print("x1 size: ", x1.size)
##
##print("x2: ")
##print(x2)
##
##print("x2 ndim: ", x2.ndim)
##print("x2 shape: ", x2.shape)
##print("x2 size: ", x2.size)
##
##print("x3: ")
##print(x3)
##
##print("x3 ndim: ", x3.ndim)
##print("x3 shape: ", x3.shape)
##print("x3 size: ", x3.size)

###Slide 14 Array Indexing: Single Element, Single Dimension
##print(x1)
##print(x1[0])
##print(x1[4])
##print(x1[-1])
##print(x1[-2])
##x1[0] = 3.14159 # will truncate
##print(x1)

###Slide 15 Array Indexing: Single Element, Multi-Dimension
##print(x2)
##print(x2[0,0])
##print(x2[2,0])
##print(x2[2,-1])

###Slide 16 Array Slicing: One Dimension
### slicing
##print(x1)
##print(x1[:3])   # up to index 3 (excl)
##print(x1[3:])   # start at index 3
##print(x1[2:5])  # element index 2 - 4
##print(x1[::2])  # every other element
##print(x1[::-1]) # reverse all

###Slide 17 Array Slicing: Multi-Dimension
### multi-slicing
##print(x2)
##
##print(x2[:2, :3]) # 2 rows, 3 columns
##
##print(x2[:3, ::2]) # all rows, every other column
##
##print(x2[::-1, ::-1]) # reverse rows and columns

#Slide 18 Accessing Array Rows and Columns
##print(x2)
##
##print(x2[:, 0])  # first column
##print(x2[0, :])  # first row
##print(x2[0])     # first row (can omit : for row)
##
###Slide 19 NumPy Arrays as Views
##print('current x2:')
##print(x2)
##x2bak = x2.copy()    # back up x2
##x2_sub = x2[:2, :2]  # slice x2 into x2_sub
##print('x2_sub:')
##print(x2_sub)
##x2_sub[0, 0]= 99     # modify x2_sub
##print('x2_sub modified:')
##print(x2_sub)
##print('x2 modified:')
##print(x2)
##x2 = x2bak.copy()    # restore original x2

###Slide 20 Reshaping Arrays
### reshape 1D to 2D (3x3)
##grid = np.arange(1, 10).reshape((3, 3))
##print('ndim:', grid.ndim, ', shape:', grid.shape)
##print(grid)

###Slide 21 Reshaping Arrays
### convert 1D array to 2D (3x1)
##print('reshape 1D array as 3x1:')
##x = np.array([1, 2, 3])
##print('x ndim:', x.ndim, ', shape:', x.shape)
##
##y = x.reshape(3, 1)
##print('y ndim:', y.ndim, ', shape:', y.shape)
##print(y)

###Slide 22 Reshaping Arrays: np.newaxis
### convert 1D to 2D (3x1) using newaxis
##print('use newaxis to reshape 1D array as 3x1:')
##x = np.array([1, 2, 3])
##print('x ndim:', x.ndim, ', shape:', x.shape)
##
##y = x[:, np.newaxis]
##print('y ndim:', y.ndim, ', shape:', y.shape)
##print(y)

###Slide 24 Array Concatenation with npconcatenate
##x = np.array([1, 2, 3])
##print('x:')
##print(x)
##
##y = np.array([3, 2, 1])
##print('y:')
##print(y)
##
##print('concatenated:')
##print(np.concatenate([x, y]))

###Slide 25 Array Concatenation with np.vstack
##x = np.array([1, 2, 3])
##grid = np.array([[9, 8, 7],
##                 [6, 5, 4]])
##
### vertically stack the arrays
##print(np.vstack([grid, x]))

###Slide 26 Array Concatenation with np.hstack
##grid = np.array([[9, 8, 7],
##                 [6, 5, 4]])
##y = np.array([[99],
##              [99]])
### horizontally stack the arrays
##print(np.hstack([grid, y]))
##
#Slide 27 Array Splitting with np.split
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3, x4 = np.split(x, [3, 5, 7])
print(x1, x2, x3, x4)

###Slide 29 Universal Functions: Example
##def compute_reciprocals(values):
##    output = np.empty(len(values))
##    for i in range(len(values)):
##        output[i] = 1.0 / values[i]
##        ##print(values[i], output[i])
##    return output
##
##values = np.random.randint(1, 10, size=5)
##print('values:', values)
##print('reciprocals:', compute_reciprocals(values))

###Slide 30 Universal Functions: Example
##import timeit
##big_array = np.random.randint(1, 100, size=1000000)
##stmt_arg = 'compute_reciprocals(big_array)' #see prev. slide
##setup_arg = 'from __main__ import compute_reciprocals, big_array'
##t = timeit.Timer(stmt=stmt_arg,
##            setup=setup_arg)
##
##print('time to run 5 reciprocal calculations on 1000000 items:')
##print(t.timeit(number=5))

###Slide 31 Universal Functions: Example
##def compute_reciprocals(values):
##    output = np.empty(len(values))
##    #for i in range(len(values)):
##    #    output[i] = 1.0 / values[i]
##    output = 1.0 / values
##    return output
##
##import timeit #from Slide 30
##big_array = np.random.randint(1, 100, size=1000000)
##stmt_arg = 'compute_reciprocals(big_array)' #see prev. slide
##setup_arg = 'from __main__ import compute_reciprocals, big_array'
##t = timeit.Timer(stmt=stmt_arg,
##            setup=setup_arg)
##
##print('time to run 5 reciprocal calculations on 1000000 items:')
##print(t.timeit(number=5))

###Slide 32 uFuncs and Array Arithmetic
##x = np.arange(4)
##print(x)
##print("x     =", x)
##print("x + 5 =", x + 5)
##print("x - 5 =", x - 5)
##print("x * 2 =", x * 2)
##print("x / 2 =", x / 2)
##print("x // 2 =", x // 2)
##
###Slide 33 uFunc Arithmetic Operators
##x = np.arange(4)
##print(x)
##print(np.add(x, 2))
##
###Slide 34 uFuncs and Arrays
##print(np.arange(5))
##print(np.arange(1, 6))
##print(np.arange(5) / np.arange(1, 6))
##
###Slide 35 uFuncs and Multi-dimensional Arrays
##x = np.arange(9).reshape((3, 3))
##print('x:\n', x)
##print('2 ** x:\n', 2 ** x)
##
###Slide 36 Specifying Output
##x = np.arange(5)
##y = np.empty(5)
##print(x)
##print(y)
##np.multiply(x, 10, out=y)
##print(y)

###Slide 37 Specifying Output: Views
##x = np.arange(5)
##y = np.zeros(10)
##print(x)
##print(y)
##np.power(2, x, out=y[::2])
##print(y)
##
###Slide 38 Aggregations
##x = np.arange(1, 6)
##print(x)
##print(np.add.reduce(x))
##print(np.multiply.reduce(x))
##
###Slide 39 Accumulating Aggregation Operation
##x = np.arange(1, 6)
##print(x)
##print(np.add.accumulate(x))
##print(np.multiply.accumulate(x))
##
###Slide 40 Aggregates as Summary Statistics
##x = np.random.random(1000000)
##print(x)
##print(np.sum(x))  # sum
##print(np.mean(x)) # average
##print(np.std(x))  # standard deviation
##
###Slide 41 Aggregates: Object Method Alternatives
##x = np.random.random(1000000)
##print(x.sum())
##print(x.mean())
##print(x.std())
##print(x.min())
##print(x.max())
##
###Slide 42 Multi-Dimensional Aggregates
##m = np.random.random((3, 4))
##print(m)
##print(m.sum())
##
###Slide 43 Aggregating on an Axis
##m = np.random.random((3, 4))
##print(m)
##print('min col = ', m.min(axis=0))
##print('max row = ', m.max(axis=1))
##
###Slide 44 Computation on Arrays: Broadcasting
##a = np.array([0, 1, 2])
##b = np.array([5, 5, 5])
##print(a + b)
##
###Slide 45 Computation on Arrays: Broadcasting
##a = np.array([0, 1, 2])
##print(a + 5)

###Slide 46 Computation on Arrays: Broadcasting
##a = np.array([0, 1, 2])
##m = np.ones((3, 3))
##print(a)
##print(m)
##print(m + a)
##
###Slide 47 Computation on Arrays: Broadcasting
##a = np.arange(3)
##b = np.arange(3)[:, np.newaxis]
##print(a)
##print(b)
##print(a + b)
##
###Slide 48 Comparisons, Masks, and Boolean Logic
##x = np.array([1, 2, 3, 4, 5])
##print(x)
##print(x < 3)
##print(x > 3)
##print(x != 3)
##print(x == 3)
##print((2 * x) == (x ** 2))
##
###Slide 49 Working with Boolean Arrays
##rng = np.random.RandomState(0)
##x = rng.randint(10, size=(3, 4))
##print(x)
##print(np.count_nonzero(x < 6))
##
#Slide 50 Logical Operators and Boolean Array Masks
##rng = np.random.RandomState(0)
##x = rng.randint(10, size=(3, 4))
##print(x)
##
##print(x[x < 6])
##print(x[x > 2])
##
##print(x[(x < 6) & (x > 2)])
##print(np.sum(x[(x < 6) & (x > 2)]))


###Slide 51 Fancy Indexing
##rng = np.random.RandomState(42)
##x = rng.randint(100, size=10)
##print(x)
##ind = [3, 7, 4]
##print(x[ind]) 
##ind = np.array([[3, 7],
##                [4, 5]])
##print(x[ind])

###Slide 52 Fancy Indexing: Multiple Dimensions
##x = np.arange(12).reshape((3, 4))
##print(x)
##
##row = np.array([0, 1, 2])
##col = np.array([2, 1, 3])
##
##print(x[row, col])

#Slide 53 - Sorting Arrays
##def selection_sort(x):
##    for i in range(len(x)):
##        swap = i + np.argmin(x[i:])
##        #print("i: ", i, "np.argmin: ", np.argmin(x[i:]), "swap: ", swap)
##        (x[i], x[swap]) = (x[swap], x[i])
##        print(x)
##    return x
##
##x = np.array([2, 1, 4, 3, 5])
##print(x)
##print(selection_sort(x))
##
###Slide 54 - Fast Sorting, new array
##x = np.array([2, 1, 4, 3, 5])
##print(x)
##print(np.sort(x))
##
###Slide 55 - Fast sorting in place
##x = np.array([2, 1, 4, 3, 5])
##save_x = x.copy()
##x.sort()
##print(save_x)
##print(x)

###Slide 56 Using argsort() for Sorted Indices
##x = np.array([22, 15, 49, 36, 57])
##i = np.argsort(x)
##print(x)
##print(i)

###Slide 57
##x = np.array([22, 15, 49, 36, 57])
##i = np.argsort(x)
##print(x)
##print(i)
##print(x[i])

###Slide 58 Sorting on Columns or Rows
### seed the random generator
##rand = np.random.RandomState(42)
##
##x = rand.randint(0, 10, (4, 6))
##print(x)
##
### sort each column of x
##print(np.sort(x, axis=0))

###Slide 59 Sorting on Columns or Rows
##rand = np.random.RandomState(42)
##x = rand.randint(0, 10, (4, 6))
##print(x)
### sort each row of x
##print(np.sort(x, axis=1))
##
#Slide 64 Partial Sorts: Partitioning
x = np.array([7, 2, 6, 4, 3, 5, 1])
print(x)
print(np.partition(x, 3))

###Slide 65 Partitioning on an Axis
##x = np.random.randint(0, 10, (4, 6))
##print(x)
##print(np.partition(x, 2, axis=1)) #1 is row, 0 is column

###--------------------------------------------------------
##
###Slide 63 - 72 all at one time
###Slide 63 K-Nearest Neighbors
## create random array of 10 2D points
##x = np.random.rand(10, 2)
##print(x)
##
###Slide 64 K-Nearest Neighbors
###import matplotlib.pyplot as plt
###import seaborn; seaborn.set() # Plot styling
##x = np.random.rand(10, 2)
##plt.scatter(x[:, 0], x[:, 1], s=100)
##plt.show()
###close the window to see the rest
##
###Slide 66 K-Nearest Neighbors
##x = np.random.rand(10, 2)
##diffs = x[:,np.newaxis,:] - x[np.newaxis,:,:]
### square the differences
##diffs_sq = diffs ** 2
### sum the squares
##dist_sq = np.sum(diffs_sq, axis=-1)
### print squared distances (rounded)
##print(dist_sq.round(decimals=3))
##
###Slide 67 K-Nearest Neighbors
### use np.argsort to sort along each row.
### leftmost columns are the indices of nearest neighbors
### leftmost column - each point is its own nearest neighbor
##print(np.argsort(dist_sq, axis=1))
##
###Slide 69 K-nearest Neighbors (K=2)
### The previous example uses a full sort.
##
### For K nearest neighbors, partition each row so
### smallest K + 1 squared distances come first, larger
### distances fill remaining positions of the array. 
##
### Use the np.argpartition function:
##K = 2
##nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
### draw lines from each point to 
### its two nearest neighbors
##
##plt.scatter(x[:, 0], x[:, 1], s=100)
##K = 2
##for i in range(x.shape[0]):
##    for j in nearest_partition[i, :K+1]:
##        # plot a line from x[i] to x[j]
##        # use some zip magic to make it happen:
##        plt.plot(*zip(x[j], x[i]), color='black')
##plt.show()

###--------------------------------------------------------
###Slide 73 - 75 all at one time
###Slide 73 Structured Data: Structured Arrays
##name = ['Alice', 'Bob', 'Cathy', 'Doug']
##age = [25, 45, 37, 19]
##weight = [55.0, 85.5, 68.0, 61.5]
### Use a compound data type for structured arrays
##data = np.zeros(4, dtype={
##        'names':('name', 'age', 'weight'),
##        'formats':('U10', 'i4', 'f8')
##       })
##data['name'] = name
##data['age'] = age
##data['weight'] = weight
##print(data)
##
###Slide 74 Creating Structured Arrays
##input('\nHit ENTER to continue')
###print(data)
##print('Names:', data['name'])     # get all names
##print('First row of data', data[0])          # get first row of data
##print(data[-1]['name']) # get name from last row
##
###Slide 75 RecordArrays
##input('\nHit ENTER to continue')
##print(data)
##data_rec = data.view(np.recarray)
##print('Ages: ', data_rec.age)
