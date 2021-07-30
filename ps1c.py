# setting up variables
total_cost = 1000000  # cost of home, fixed
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
starting_salary = float(input("Enter your annual salary: $"))
target = portion_down_payment * total_cost

while abs(current_savings - target) > threshold and guess < 9999:
    annual_salary = starting_salary
    # computes the amount saved for a guess
    for i in range(1,37):
        if i > 0 and i % 6 == 0:
            annual_salary += annual_salary * semi_annual_salary_raise
        current_savings += current_savings * r / 12
        current_savings += (guess/10000) * (annual_salary / 12)

    if current_savings < target - threshold:
        low = guess
    elif current_savings > target + threshold:  # current rate saves too much money
        high = guess
    else:
        print("Best savings rate: " + str(guess / 10000))
        break
    guess = int((low + high) / 2)
    steps += 1
    current_savings = 0

if guess < 9999:  # if loop ended with valid rate
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")
