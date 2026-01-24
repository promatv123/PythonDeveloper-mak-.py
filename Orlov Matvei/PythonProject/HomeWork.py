N = int(input("введите ваше число : "))


print("нечетные числа :")
for i in range(1, N + 1, 2):
    print (f"{i}")

print("четные числа :")
for i in range(2, N + 1, 2):
    print (f"{i}")

