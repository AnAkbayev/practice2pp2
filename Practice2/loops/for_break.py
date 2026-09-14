# For Loop Break
# Example 1: Stop the loop at 3.
for number in range(1, 6):
    print(number)
    if number == 3:
        break

# Example 2: Stop when a word is found.
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)

# Example 3: Find a number.
numbers = [10, 20, 30, 40]
for number in numbers:
    if number == 30:
        print("Found 30")
        break

# Example 4: Stop at the first multiple of 7.
for number in range(1, 50):
    if number % 7 == 0:
        print("First multiple:", number)
        break

# Example 5: Stop after three iterations.
count = 0
for item in ["A", "B", "C", "D", "E"]:
    print(item)
    count += 1
    if count == 3:
        break
