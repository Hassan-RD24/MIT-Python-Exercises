# Part A

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = total_cost * 0.25
current_savings = 0.0
r = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings * r / 12) + ((annual_salary / 12) * portion_saved)
    months += 1

print("Number of months:", months)


#***********************************************************************************************************


# Part B

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float (input ("Enter semi_annual_raise: "))

portion_down_payment = total_cost * 0.25
current_savings = 0.0
r = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings * r / 12) + ((annual_salary / 12) * portion_saved)
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise


print("Number of months:", months)



#***********************************************************************************************




# Part C

annual_salary = float(input("Enter the starting salary: "))

semi_annual_raise = 0.07
investment_rate = 0.04
down_payment_fraction = 0.25
house_cost = 1000000
down_payment = down_payment_fraction * house_cost

# check if saving 100% of salary is even enough
current_salary = annual_salary
portion_down_payment = 0
for month in range(36):
    monthly_salary = current_salary / 12
    portion_down_payment += monthly_salary * 1.0
    portion_down_payment += portion_down_payment * (investment_rate / 12)
    if (month + 1) % 6 == 0:
        current_salary += current_salary * semi_annual_raise

if portion_down_payment < down_payment - 100:
    print("It is not possible to pay the down payment in three years.")
else:
    low = 0
    high = 10000
    steps = 0
    best_rate = None

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000

        current_salary = annual_salary
        portion_down_payment = 0
        for month in range(36):
            monthly_salary = current_salary / 12
            portion_down_payment += monthly_salary * rate
            portion_down_payment += portion_down_payment * (investment_rate / 12)
            if (month + 1) % 6 == 0:
                current_salary += current_salary * semi_annual_raise

        if abs(portion_down_payment - down_payment) <= 100:
            best_rate = rate
            break
        elif portion_down_payment < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    print("Best savings rate:", best_rate)
    print("Steps in bisection search:", steps)
























