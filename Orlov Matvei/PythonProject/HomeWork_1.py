N = int(input("Введите ваше число:"))

summa = 0


for i in range(1, N + 1 ):
    summa += i

print(f"сумма числа от 1 до {N} равна: {summa}")