import random
a = 0
b = 0
while a < 3 and b <3:
    c = random.randint(0,10)
    d = random.randint(0,10)
    s = c + d
    print(c, "+", d , "= ")
    f = int(input("Введите ответ: "))
    if f == s:
        a = a + 1
        b = 0
        print("Верно", "WinStreak ", a )
    else:
        b += 1
        a = 0
        print("Неверно", "LoseStreak ", b)
else:
    if a == 3:
        print("Win")
    elif b == 3:
        print("Lose")

