#
n = int(input('введите целое число: '))
if n % 1 != 0:
   print('вы ввели некорректное число')
   exit()
for i in range(2, n, 1):
   if i < n**(1/2):
      print ('число  не простое')
      exit()
print('число простое')