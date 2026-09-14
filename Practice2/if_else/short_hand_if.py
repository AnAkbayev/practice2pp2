# Short Hand If Else (conditional expression)
# Example 1: One-line if.
age = 20
if age >= 18: print("Adult")

# Example 2: One-line if-else.
age = 16
print("Adult") if age >= 18 else print("Minor")

# Example 3: Assign a value using a conditional expression.
number = 7
result = "even" if number % 2 == 0 else "odd"
print(result)

# Example 4: Choose the larger number.
a = 10
b = 20
larger = a if a > b else b
print(larger)

# Example 5: Conditional expression with strings.
logged_in = True
message = "Welcome!" if logged_in else "Please log in."
print(message)
