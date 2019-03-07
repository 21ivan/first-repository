# 1. Сворити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

a = [x for x in range(21)]
print(a)
print(max(a))
print(min(a))
num_list = [int(input('enter int {}:'.format(i+1)))for i in range(6)]
print(num_list)
print('max num - ', max(num_list))
print('min num - ', min(num_list))

###############
# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.
for x in (range(1, 11)):
    if x%2==0:
        print(x,' - is even multiple of 2')
    elif x%3 == 0:
        print(x,' - is an odd multiple of 3')
    else:
        print(x,' - not divisible by 2 and 3')

################
# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
n = int(input('Enter number - '))
factorial = 1
if n < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif n==0:
    print('The factorial of the number 0 is 1')
else:
    for i in range(1, n+1):
        factorial=factorial*i
    print ('factorial of {0} is {1}'.format(n,factorial))

####################
# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)
print('Hello, please input your Log in')
log = input("Enter Username: ")

while log!='First':
    print('Error: wrong username, please try one more time.')
    log = input("Enter Username: ")
    print(log)

print('Access granted!')
print('Greeteng,', log)

################################
# 5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).
a = int(input('Enter numbers:'))
while a!=0:
    if a<0:
        print('There was negative number:', a)
        break
    a = int(input("Enter next number:"))
    if a==0:
        print('no negative number founded!')
        break
    else:
        print('no negative number founded')

######################################
# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
# (наприклад 10 equals 2 * 5
#                     11 is a prime number
#                     12 equals 2 * 6
#                     13 is a prime number
#                     14 equals 2 * 7
#                      ………………….)
for c in range(10, 31):
    print(c, 'is a prime number' if c%2!=0 else 'equals 2*', int(c/2))

########################################
# 8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)
string1 = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
print(string1)
string1 = string1.split()
string2=''
string2 = [string2 + ' ' + i for i in sorted(string1, key = lambda a: len(a))]
print(string2)