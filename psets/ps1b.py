# setting up variables
total_cost = None # cost of dream home, will ask user
portion_down_payment = 0.25 # must pay 25% of total cost upfront
current_savings = 0
r = 0.04 # rate of return on investment
annual_salary = None # will ask user
portion_saved = None # percentage of salary dedicated to down payment
months = 0
semi_annual_salary_raise = None # raise every six months

# asking for user input
annual_salary = float(input("Enter your annual salary: $"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_salary_raise = float(input("Enter the semi-annual raise, as a decimal: "))

while(current_savings <= portion_down_payment * total_cost):
    if months > 0 and months % 6 == 0:
        annual_salary += annual_salary * semi_annual_salary_raise
    current_savings += current_savings * r / 12
    current_savings += portion_saved*(annual_salary/12)
    months += 1

print("Number of months:", months) # added a comment