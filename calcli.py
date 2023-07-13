num_1 = "Enter your first number: "
num_2 = "Enter your second number: "
method = "add, subtract, multiply or divide? please choose one: "
result = "The result is:"

if method == "add":
  print(result, num_1 + num_2)
elif method == "subtract":
  print(result, num_1 - num_2)
elif method == "multiply":
  print(result, num_1 * num_2)
elif method == "divide":
  print(result, num_1 / num_2)
else:
  print("Invalid! try again!")
