"""
Задача 3. Создайте класс Матрица.
Добавьте методы для: - вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
"""
import numpy as np

class Matrix:
    """ Класс матрица """
    rows = None
    columns = None

    def __init__ (self, matrix):
        """ Конструктор принимает:

        :param rows: количество строк
        :param columns: количество столбцов
        :param matrix: список из списков 

        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __add__ (self, other):
        """ Метод производит сложение 2х матриц.

        :param other: Matrix

        :raises ValueError: if self.rows != other.rows or self.columns != other.columns

        :rtype str
        :return сложение 2х матриц
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError ('Матрицы разные, сложение не возможно')
        res_matrix = [[0 for _ in range(self.columns)] for _ in range (self.rows)]
        for i in range (self.rows):
            for j in range (self.columns):
                res_matrix [i][j] = self.matrix[i][j] + other.matrix[i][j] 
        return res_matrix


    def __mul__ (self, other):
        """ Метод производит умножение 2х матриц.

        :param other: Matrix

        :rtype str
        :return умножение 2х матриц
        """
        res = np.dot (self.matrix,other.matrix)
        return res

    def __eq__(self, other: "Matrix"):
        """ Метод производит сравнение 2х матриц путем сравнения каждого элемента матрицы.

        :param other: Matrix

        :raises ValueError: if self.rows != other.rows or self.columns != other.columns

        :rtype bool
        :return сложение 2х матриц
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError ('Матрицы разные, сравнить их не возможно')
        for i in range (self.rows):
            for j in range (self.columns):
                if self.matrix[i][j] != other.matrix[i][j]: 
                    return False
        return True


    def __str__(self):
        return f'({self.matrix})'


if __name__ == "__main__":
    matrix_1 = Matrix([[4, 7, 1, 2 ], [8, 4, 2, 9], [10, 13, 12, 2]])
    matrix_2 = Matrix([[4, 7, 1, 2 ], [8, 4, 2, 9], [10, 13, 12, 2]])
    print(f"Результат сложения матриц {matrix_1 + matrix_2}")
    print(type(matrix_1))

    matrix_3 = Matrix([[4, 7, 1, 2 ], [8, 4, 2, 9], [10, 13, 12, 2]])
    matrix_4 = Matrix([[4, 7, 1 ], [8, 4, 2], [10, 13, 12], [13, 2, 4]])
    print(f"Результат перемножения матриц\n{matrix_3*matrix_4}")
    print(matrix_1 == matrix_2)
    
    print (Matrix.__doc__)
    print (matrix_1.__doc__)
    print (matrix_1.__add__.__doc__)