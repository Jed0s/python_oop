"""
Задача: перегрузить оператор сложения
"""

class Rope:
    def __init__(self, l):
        self.length = l

    def __str__(self):
        return str(self.length)

    def __add__(self, other):
        if isinstance(other, self.__class__): # второй объект того же класса
            return Rope(self.length + other.length)
        elif isinstance(other, (int, float)): # второй объект - число
            return Rope(self.length + other)
        else:
            raise TypeError


class Rectangle:
    def __init__(self, w, h, s):
        self.width = int(w)
        self.height = int(h)
        self.sign = str(s)
    def __str__(self):
        rect = []
        for i in range(self.height):
            rect.append(self.sign * self.width)
        rect = '\n'.join(rect)
        return rect
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height, self.sign)


# output for first class
rope = Rope(19)
rope2 = Rope(29)
print(rope)
print(rope.__add__(11))
print(rope.__add__(rope2))

#output for second class
a = Rectangle(4,2,'*')
b = Rectangle(8,3,'$')
print(a+b)
print(b+a)