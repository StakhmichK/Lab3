a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

print(f"Integers from {a} to {b} that \
       are multiples of {c}:")

for i in range(a, b + 1):
    if i % c == 0:
        print(i)