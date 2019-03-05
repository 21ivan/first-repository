a=0
while a<=100:
    if a%2==0:
        print('Even numbers:\n', a)
    a+=1

###########################

list_number=[]
print("List of even number: ")
for a in range(2, 101):
    if a%2==1:
        list_number.append(a)
print(list_number)

##################################

list_number=[4, 2, 4, 3]
contain_odd = False
for item in list_number:
    if not item%2==0:
        contain_odd = True
        break
if contain_odd:
    print('There are odd numbers in the list')
else:
    print('There are only even numbers in the list')

###########################

list_number=[1,5,7,9,0,6,5]
list_number2=[]
for a in range(len(list_number)):
    list_number[a]=float(list_number[a])
print(list_number)

##################################

a=1
b=1
n=int(input('Enter the number - '))
i=0
while i<n-2:
    fib_sum = a + b 
    a=b
    b=fib_sum
    i+=1
    print(b) 

##################################

list_str = ['adsd', 'bd', 'dsfc', 'sssdsdsd']
for item in list_str:
    print(item)