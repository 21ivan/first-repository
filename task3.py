a = int(input('a - '))
b = int(input('b - '))

def nsd (a, b):
    if a%b==0:
        return b
    else:
        return nsd(b, a%b)
print('nsd - ', nsd(a, b))


nsk = a * b // nsd(a, b)
print('nsk - ', nsk)