'''
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников
по площади
Должны работать все шесть
операций сравнения
'''


class Rectangle:
    """ Класс Архив"""

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        """ конструктора класса 

        :param length_cm: длина прямоугольника
        :param width_cm: ширина прямоугольника
        """
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        """ Расчет периметра прямоугольника """
        return (self.width + self.length) * 2

    def calc_square(self):
        """ Расчет площади прямоугольника """
        return self.width * self.length

    def __add__(self, other):
        """ сложение 2х прямоугольников

        :param other: Rectangle

        :return: периметр 2х треуголтников
        """
        return Rectangle(length_cm=(self.length + other.length),
                         width_cm=self.width)

    def __sub__(self, other):
        """ Вычетание 2х прямоугольников

        :param other: Rectangle

        :return: периметр 2х треуголтников
        """
        return Rectangle(length_cm=abs(self.length - other.length),
                         width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        """ сравнение 2х прямоугольников на равенство

        :param other: Rectangle

        :rtype: bool
        :return: результат сравнения прямоугольников
        """
        return self.calc_square() == other.calc_square()

    def __lt__(self, other: "Rectangle"):
        """ сравнение первый прямоугольник строго меньше второго

        :param other: Rectangle

        :rtype: bool
        :return: результат сравнения прямоугольников
        """
        return self.calc_square() < other.calc_square()

    def __gt__(self, other: "Rectangle"):
        """ сравнение первый прямоугольник строго болше второго

        :param other: Rectangle

        :rtype: bool
        :return: результат сравнения прямоугольников
        """
        return self.calc_square() > other.calc_square()

    def __ge__(self, other: "Rectangle"):
        """ сравнение первый прямоугольник болше или равен второму

        :param other: Rectangle

        :rtype: bool
        :return: результат сравнения прямоугольников
        """
        return self.calc_square() >= other.calc_square()

    def __le__(self, other: "Rectangle"):
        """ сравнение первый прямоугольник меньше или равен второму

        :param other: Rectangle

        :rtype: bool
        :return: результат сравнения прямоугольников
        """
        return self.calc_square() <= other.calc_square()


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
                   width_cm=2)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_square() = }')
    print('---')

    r2 = Rectangle(length_cm=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_square() = }')

    r3 = r2 + r1

    print('---')
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_square() = }')

    print(r1 == r2)
    print(r1 <= r2)
    print(r1 >= r2)

    print(Rectangle.__doc__)
    print(r1.__doc__)
    print(r1.__eq__.__doc__)
