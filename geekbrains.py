user = int(input("Введите время в секундах"))
n = user % 10
m = user // 10

while n > 0:
    if n > m:
        max = n
    else:
        max = m

print(f"{max}")