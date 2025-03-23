s = ""
while True:
    a = input("Введите слово: ")
    s += a + " "
    if a.lower() == "stop":
        break
print(s)
