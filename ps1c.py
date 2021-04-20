# setting up variables
total_cost = 1000000  # cost of dream home, fixed
portion_down_payment = 0.25 # must pay 25% of total cost upfront
current_savings = 0
r = 0.04 # rate of return on investment
annual_salary = None # will ask user
months = 0
semi_annual_salary_raise = 0.07 # raise every six months
threshold = 100 # how far off the approximation can be
low = 0
high = 10000
guess = high/2
steps = 0

# asking for user input
annual_salary = float(input("Enter your annual salary: $"))

while abs(current_savings - portion_down_payment * total_cost) > threshold:
    for i in range(1,36):
        current_savings += current_savings * r / 12     # calculate interest
        if i % 6 == 0:  # twice a year, give the semi-annual raise
            annual_salary *= semi_annual_salary_raise
        current_savings += guess * (annual_salary / 12)     # add new portion of salary
    if current_savings + 100 < portion_down_payment * total_cost:
        high = guess
    if current_savings - 100 > portion_down_payment * total_cost:
        low = guess
    guess = (low + high) / 2
    steps += 1

print("Best savings rate:" + guess/10000)