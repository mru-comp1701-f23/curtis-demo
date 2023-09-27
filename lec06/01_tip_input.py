TIPOUT = 0.02
num_employees = int(input("How many employees on shift? "))
sales = float(input("What was the total sales? "))
tips = sales * TIPOUT / num_employees
# concatenation with type casting
print("Everyone takes home $" + str(tips))