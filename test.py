import numpy as np

def mul (self, other):
    res = np.dot (self,other)
    return res


matrix_3 = ([[4, 7, 1, 2 ], [8, 4, 2, 9], [10, 13, 12, 2]])
matrix_4 = ([[4, 7, 1 ], [8, 4, 2], [10, 13, 12], [13, 2, 4]])

print(mul(matrix_3,matrix_4))