TIP_PERCENT = 0.02
total_sales = 8000
num_employees = 6
# TIP_PERCENT = 0.7 # Don't do this - constants should only be defined once!

total_tips = total_sales * TIP_PERCENT
tip_per_employee = total_tips / num_employees
print("Each employee gets $", tip_per_employee, sep = "")