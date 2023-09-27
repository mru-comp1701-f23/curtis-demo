TIPOUT = 0.02
num_employees = int(input("How many employees on shift? "))
sales = float(input("What was the total sales? "))
tips = sales * TIPOUT / num_employees
# printing with f-string
print(f"Everyone takes home ${tips:.2f}")
# rounding almost behaves the same way, but doesn't show extra 0s
print(round(tips, 2))