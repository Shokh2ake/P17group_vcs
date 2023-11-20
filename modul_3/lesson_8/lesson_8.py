# import numpy as np


# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
#
# print(type(arr))


# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# print(arr[1, 0])


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(arr[1, 1, 2])



# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# arr = np.array([1, 2, 3, 4], ndmin=5)
#
# print(arr)
# print('number of dimensions :', arr.ndim)


# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 2])



# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 1:4])

# arr = np.array([1, 2, 3, 4])
#
# print(arr.dtype)


# arr = np.array([1, 2, 3, 4], dtype='S')
#
# print(arr)
# print(arr.dtype)


# arr = np.array([1, 2, 3, 4], dtype='i4')
#
# print(arr)
# print(arr.dtype)

# arr = np.array([1, 0, 3])
#
# newarr = arr.astype(bool)
#
# print(newarr)
# print(newarr.dtype)




# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
#
# print(arr)
# print(x)



# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#
# print(arr.shape)


# arr = np.array([41, 42, 43, 44])
#
# filter_arr = arr % 2 == 0
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)









