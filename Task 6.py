import random
# Create an array of 20 integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(20)]

even = []
odd = []

# Separate odd and even numbers
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# Display results
print("Original Array:")
print(numbers)

print("\nEven Numbers:")
print(even)

print("\nOdd Numbers:")
print(odd)