# Boolean Operators: and, or, not
# Example 1: AND is True only when both conditions are True.
age = 20
has_id = True
print(age >= 18 and has_id)

# Example 2: OR is True when at least one condition is True.
is_weekend = True
is_holiday = False
print(is_weekend or is_holiday)

# Example 3: NOT reverses a Boolean value.
is_raining = False
print(not is_raining)

# Example 4: Combine comparisons with AND.
temperature = 22
print(temperature > 15 and temperature < 30)

# Example 5: Combine several Boolean expressions.
username = "admin"
password_correct = True
print((username == "admin") and password_correct)
