#создаем независимую переменную
number1 = float(input("Введите расстояние в сантиметрах"))
#создаем зависимые переменные
number2 = number1 / 2.54 #дюймы
number3 = number2 / 12 #футы
number4 = number3 / 3 #ядра
number5 = number4 / 1760 #мили
#Выводим переменные
print(number1 , "это" , number2 , "дюймов")
print(number1 , "это" , number3 , "футов")
print(number1 , "это" , number4 , "ядер")
print(number1 , "это" , number5 , "миль")
