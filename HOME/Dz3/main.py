# Задание 1
# Запросить у пользователя его возраст и определить, кем он
# является: ребенком (0–2), подростком (12–18), взрослым
# (18_60) или пенсионером (60– ...).

# x = int(input("укажите ваш возраст: "))
# if x <= 2 :
#     print("ребенок")
# elif x <= 18:
#     print("подросток")
# elif x <= 60:
#     print("взрослый")
# elif x >= 61:
#     print("пенсионер")
# else:
#     print("введите корректное значение")

# Задание 2
# Запросить у пользователя число от 0 до 9 и вывести ему
# спецсимвол, который расположен на этой клавише (1–!,
# 2–@, 3–# и т. д).

# x = int(input("введите число от 0 до 9: "))
# if x == 0 :
#     print(")")
# elif x == 1:
#     print("!")
# elif x == 2:
#     print("@")
# elif x == 3:
#     print("#")
# elif x == 4:
#     print("$")
# elif x == 5:
#     print("%")
# elif x == 6:
#     print("^")
# elif x == 7:
#     print("&")
# elif x == 8:
#     print("*")
# elif x == 9:
#     print("(")
# else:
#     print("введите корректное значение")

# Задание 3
# Запросить у пользователя трехзначное и число и проверить,
# есть ли в нем одинаковые цифры.

# x = int(input("введите трехзначное число: "))
# if x // 100 == x // 10 % 10:
#    print('Да')
# elif x // 100 == x % 10:
#    print('Да')
# elif x // 10 % 10 == x % 10:
#    print('Да')
# else:
#    print('Нет')

# Задание 4
# Запросить у пользователя год и проверить, високосный он
# или нет. Високосный год либо кратен 400, либо кратен 4 и
# при этом не кратен 100.

# x = int(input("Введите год: "))
# if x % 4 == 0:
#     print("Високосный")
# elif x % 100 == 0:
#     if x % 400 == 0:
#         print("Обычный")
#     else:
#         print("Високосный")
# else:
#     print("Обычный")

# Задание 5
# Запросить у пользователя пятиразрядное число и определить, является ли оно палиндромом.

# x = int(input("Введите пятизначное число для проверки на палиндром: "))
# a = x // 10000
# b = x % 10000 // 1000
# c = x % 10
# d = x % 100 // 10
# if a == c and b == d:
#     print("палиндром")
# else:
#     print("не палиндром")

# Задание 6 
# Написать конвертор валют. Пользователь вводит количество USD, выбирает, в какую валюту хочет перевести: EUR,
# UAN или AZN, и получает в ответ соответствующую сумму.

# x = int(input("введите количество USD: "))
# s = int(input("в какую валюту вы хотите перевести 0 - EUR, 1 - UAN, 2 - AZN "))
# if s == 0:
#     print(x * 0.93145)
# elif s == 1:
#     print(x * 7.06)
# elif s == 2:
#     print(x * 1.7)
# else:
#     print("введите корректное значение")

# Задание 7 
# Запросить у пользователя сумму покупки и вывести сумму
# к оплате со скидкой: от 200 до 300 – скидка будет 3%, от 300
# до 500 – 5%, от 500 и выше – 7%.

# x = int(input("введите сумму покупки: "))
# if x >= 200 and x <= 300:
#     a = x - x * 0.03
#     print("сумма со скидкой: ", a)
# elif x > 300 and x <= 500:
#     b = x - x * 0.05
#     print("сумма со скидкой: ", b)
# elif x > 500:
#     c = x - x * 0.07
#     print("сумма со скидкой: ", c)

# Задание 8 
# Запросить у пользователя длину окружности и периметр
# квадрата. Определить, может ли такая окружность поместиться в указанный квадрат. 

# x = int(input("введите длину окружности: "))
# y = int(input("введите периметр квадрата: "))
# if x * 2 * (0.5) < 2 * y:
#     print("Поместится") 
# else:
#     print("Не поместится")

# Задание 9 
# Задать пользователю 3 вопроса, в каждом вопросе по 3 варианта ответа. За каждый правильный ответ начисляется 2
# балла. После вопросов выведите пользователю количество
# набранных баллов.

print("Зимой и летом одним цветом:\n", "1-ёлка\n", "2-палка\n", "3-тёрка\n")
answer = (input("Введите 1,2,3 :\n"))
score = 0
if answer == 1: 
    print(f"Вы выбрали верно, получи 2 бала")
    score = score + 2
else:
    print("Ответ не верный")
    
# print("У Вас очков: " , score)

# q1 = input("Зимой и летом одним цветом: ")
# score = 0
# if q1 == "ёлка" or q1 == "елка":
#     print("Ответ верный")
#     score = score + 2
# else:
#     print("Ответ не верный")
    
# q2 = input("Висит груша нельзя скушать: ")
# if q2 == "лампочка":
#     print("Ответ верный")
#     score = score + 2
# else:
#     print("Ответ не верный")
    
# q3 = input("Что выше леса поднимается да без огня горит: ")
# if q3 == "солнце":
#     print("Ответ верный")
#     score = score + 2
# else:
#     print("Ответ не верный")

# q4 = input("Без рук, без ног, А ворота открывает: ")
# if q4 == "ветер":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")
# q5 = input("На дворе горой, а в избе водой: ")
# if q5 == "снег":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ не верный")
# print("У Вас очков: " , score)

