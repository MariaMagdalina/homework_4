# данная программа сформировывает случайным образом список коэффициентов (значения от 0 до 100) многочлена и записывает в файл многочлен степени k (натуральная степень).
from random import randint
k = int(input('введите степень многочлена: '))
koeff = []    # список коэффициентов
for i in range(k+1):
   koeff.append(randint(0, 100))  
polynom = ''
for i in range(k+1):
   if (k - i) == 0:
      polynom = polynom + """ + """ + str(koeff[i]) + """ = 0"""
   elif (k - i) == 1:
      polynom = polynom + """ + """ + str(koeff[i]) + """x""" 
   elif koeff[i] == 0:
      polynom = polynom + """"""
   elif koeff[i] == 1:
      polynom = polynom + """ + """ + """x^""" + str(k - i) 
   elif i == 0:
      polynom = polynom + str(koeff[i]) + """x^""" + str(k - i)
   else:
      polynom = polynom + """ + """ + str(koeff[i]) + """x^""" + str(k - i) 
f = open('file.txt', 'w')
f.write(polynom)
f.close()