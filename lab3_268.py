n = int(input("Enter the number: ").strip())

if n < 1 or n > 9:
    print("n must be a natural number from 1 to 9")

for i in range(1, n + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(j)
        
    print(line)