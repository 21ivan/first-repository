# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.
def med_arith(first,*values):
    """This function calculators"""
    return((first + sum(values))/(1+len(values)))
    print(med_arith(3, 4, 4, 4)

# 2.  Написати функцію, яка повертає абсолютне значення числа
def absolute_values(a):
    """tHIS FUNCTON RETURN ABSOLUTE VALUES"""
    if a >= 0:
        return a
    else:
        return -a
print(absolute_values(-7))

# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації DocStrings.
def printmax(x,y):
    """This function find max values """
    x=int(x)
    y=int(y)

    if x>y:
        print('max= ', x)
    elif x==y:
        print(x, 'is equal to', y)
    else:
        print('min= ', y)
printmax(5,10)
print(printmax.doc)

# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача.
def rectangle ():
    a = float(input('input width: '))
    b = float(input('input height: '))
    print('Square={}'.format(a*b))

def triangle():
    a = float(input('input basis: '))
    h = float(input('input height: '))
    print('Square={}'.format(0.5*a*h))

def circle():
    r = float(input('input radius: '))
    print('Square={}'.format(3.14*r**2))

figure = input('1-rectangle, 2-triangle, 3-circle\n')
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()
elif figure == '3':
    circle()
else:
    print('Input error')

# 5.  Написати функцію, яка обчислює суму цифр введеного числа.
from functools import reduce
list = input ('input number:\n')
def sum_of_numbers(list):
    """this function calculates the sum of the entered numbers"""
    return reduce(lambda x, y: x+y, list)
print(sum_of_numbers)    

# 6.  Написати програму калькулятор, яка складається з наступних функцій: 

# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, 
# калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, 
# користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!
sum = lambda x, y: x + y
product = lambda x, y: x * y
difference = lambda x, y: x - y
division = lambda x, y: x / y

def calculator():
    while True:
        x = float(input('enter first number: '))
        y = float(input('enter second number: '))
        choise = input('1 - sum;\n2 - product;\n3 - difference;\n4 - division;\n0 - exit.\n')
        if choise == '1':
            print(sum(x,y))
        elif choise == '2':
            print(product(x,y))
        elif choise == '3':
            print(difference(x, y))
        elif choise == '4':
            print(division(x,y))
        elif choise == '0':
            print('Thank you for choosing our software ')
            break
        else : 
            continue
calculator()

# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.

def fibonacci(n):
    """This function calculates """
    if n in (1,2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння
def discriminant():
    print('scheme of the equation: a(x**2) + bx + c')
    a = int(input('enter a:\n'))
    b = int(input('enter b:\n'))
    c = int(input('enter c:\n'))
    print('discriminant={}'.format(b**2 - 4 * a * c))
discriminant()
