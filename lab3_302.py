a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a <= b:
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            print(i, end=' ')