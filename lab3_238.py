k = float(input("Enter the current exchange rate (UAH per USD): "))
n = int(input("Enter how many dollars to convert: "))

print("\nTable of USD to UAH conversion:")
print("USD\tUAH")
print("----------------")

for i in range(1, n + 1):
    uah = i * k
    print(f"{i}\t{uah:.2f}")