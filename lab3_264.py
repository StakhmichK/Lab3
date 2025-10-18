n = int(input("Enter the number of quiz \
participants: "))

max_correct = 0      
has_zero = False 

for i in range(1, n + 1):
    correct = int(input(f"Enter the number of \
correct answers for participant #{i}: "))
    if correct > max_correct:
        max_correct = correct

    if correct == 0:
      has_zero = True    

print(f"\nThe winner answered {max_correct} \
questions correctly.")

if has_zero:
    print("Yes")
else:
      print("No")