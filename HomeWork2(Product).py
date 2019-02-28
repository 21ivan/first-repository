num=(input('input number\n'))

c=tuple(num)

prod=int(c[0])*int(c[1])*int(c[2])*int(c[3])
print('Revers:\n', num[::-1])
print('Sorted:\n', sorted(c))
print('Product is - ', prod)
