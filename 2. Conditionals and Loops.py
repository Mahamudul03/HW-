# Input
number = int(input("Enter a number: "))

# Check if the number
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Calculate the sum
sum_even = sum(i for i in range(1, number + 1) if i % 2 == 0)
print("Sum of all even numbers:", sum_even)
