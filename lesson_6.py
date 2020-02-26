"""
Задача: Разработать класс с "полной инкапсуляцией", доступ к атрибутам которого и изменение данных реализуется через вызовы методов.
"""

class FullCapsul:
    def __init__(self, n, a, s):
        self.__name = FullCapsul.__testStr(n)
        self.__age = FullCapsul.__testInt(a)
        self.__sex = FullCapsul.__testStr(s)
    def setName(self, n):
        self.__name = FullCapsul.__testStr(n)
    def setAge(self, a):
        self.__age = FullCapsul.__testInt(a)
    def setSex(self, s):
        self.__sex = FullCapsul.__testStr(s)
    def getName(self):
        return "Name: {0}".format(self.__name)
    def getAge(self):
        return "Age: {0}".format(self.__age)
    def getSex(self):
        return "Sex: {0}".format(self.__sex)
    def __testStr(value):
        if value == "":
            print("No value found.")
            pass
        else:
            return value
    def __testInt(value):
        if value < 0:
            print("No  right value found.")
            pass
        else:
            return value
    def __str__(self):
        return "Name: {0} | Age: {1} | Sex: {2}".format(self.__name, self.__age, self.__sex)

unit1 = FullCapsul("Kira", 23, "F")
print(unit1)
unit2 = FullCapsul("Ruslan", 19, "M")
print(unit2.getName())
print(unit2.getAge())
unit1.setAge(17)
print(unit1)