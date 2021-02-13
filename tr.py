def shift(massLen, num):
    mass = list(range(1, massLen + 1))
    if num < 0:
        for i in range(0, int(str(num)[1:len(str(num))])):
            mass.append(mass.pop(0))
        print(mass)
    else:
        for i in range(num):
            mass.insert(0, mass.pop())
        print(mass)


while True:
    try:
        massLen = int(input("Сколько чисел хотите в массиве?: "))
        number = int(input("Введите число для сдвига: "))
        shift(massLen, number)
    except ValueError:
        print("Введите цифру а не букву!")