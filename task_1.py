# Вычислить число c заданной точностью d
from decimal import Decimal
print(Decimal(input('задайте число: ')).quantize(Decimal(Decimal(input('задайте точность: ')))))