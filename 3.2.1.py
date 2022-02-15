# Напишите программу подсчета букв ‘a’ в строке «abrakadabra»

str = "abrakadabra"

count = 0
for symb in str:
    if symb == 'a':
        count += 1

print("Кол-во \"a\" = ", count, end="")

# или print("abrakadabra".count('a')), но я не знал, что так можно
