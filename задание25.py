x, y, n = map(int,input("Введите числа:").split())
name = (x * 100 + y) * n #переведем цену в копейки и умножим на количество
name1 = name // 100
name2 = name % 100
print(f"{name1}рублей,{name2}копеек")
