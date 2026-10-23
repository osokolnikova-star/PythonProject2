import math
a = int(input("Введите любое число: "))
b = int(input("Введите любое число: "))
r = max(a, b)
n = min(a, b)
result = math.pi * (r**2 - n**2)
print(result)