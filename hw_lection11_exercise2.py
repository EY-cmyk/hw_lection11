import math
a = int(input("A:"))
b = int(input("b:"))
c = int(input("c:"))

class Mathematikian():
    pass
    def square_nums(self):
        return a*a, b*b, c*c
    def remove_positives(self):
        return -a, -b, -c
    def filter_leaps(self):
        if a / 4 and a / 100:
            print(a)
        elif b / 4 and b / 100:
            print(b)
        elif c / 4 and c / 100:
            print(c)
        else:
            print("zero")
        

my_class = Mathematikian()
print(my_class.square_nums())
print(my_class.remove_positives())
my_class.filter_leaps()