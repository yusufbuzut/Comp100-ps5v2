# Your solution for part d

montly_salary= float(input("Enter your monthly salary:"))
total_cost= float(input("Enter the cost of the dream car:"))
percentage_increase= float(input("Enter the increase in the car's price, as a decimal:"))
interest_rate= 0.01
percentage_salary_increase= float(input("Enter the percentage salary raise, as a decimal:"))

first_salary= montly_salary

epsilon= 1000
low=0
high=10000

num_guesses=0 

current_savings= 0

total_cost= total_cost*(1+percentage_increase)
while abs(current_savings - total_cost) > epsilon :
  guess= (low+high)/2
  current_savings=0
  montly_salary= first_salary
  for n in range(24):
    current_savings= current_savings*(1+interest_rate)
    current_savings= current_savings+(montly_salary*guess/10000)
    n= n+1
    if n % 6 == 0:
      montly_salary= montly_salary*(1+percentage_salary_increase)
  if abs(current_savings - total_cost) <= epsilon:
      break
  elif   current_savings > total_cost:
      high = guess
  elif   current_savings < total_cost:
      low = guess
  if low == high:
    break
  num_guesses = num_guesses + 1
if guess<= 9999:
  print("Best savings rate: {:.3f}".format(guess/10000))
  print("Steps in bisection search:", num_guesses)
else :
  print('It is not possible to buy the car in two years')
  

