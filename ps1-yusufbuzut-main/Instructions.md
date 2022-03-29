# PS1 - Your Dream Car
# Deadline: 01/11/2020-23:00

## Introduction

This problem set focuses on the Python control flow for solving a computational problem. Moreover, you will have a chance to practice *Bisection Search*. This problem set includes **four** different problems. For each part, you should save your code as ps1{name of the part}. For example, for part D, it should be ps1d.py.

Assume that you have finished your school with a great success and you have a great job in great company. As you get paid, you want to buy something with your savings. Since house prices are very high in Istanbul, you think it will take nearly fifty years to buy a house. Therefore, you want to buy something cheaper. Since childhood, you have great interest in cars and you have a dream car. You decided to save your salary to buy your dream car.

In each part of this problem set, we will explore different kinds of mini problems where we have one goal which is buying your dream car.

---

## Parts

1. Buying the car in an unrealistic scenario
2. A new model that is more expensive
3. Good news: Salary raise!
4. The fastest way to save for the car

---

## PART A. Buying the car in an unrealistic scenario

In this part, you will calculate how many months it takes to buy your dream car with the given inputs such as your monthly salary, what percentage of the salary that you will save each month and the cost of the car. The reason we call it an unrealistic scenario is that we assume neither the car's price nor your salary changes during this time. 

* Call the cost of the car `total_cost`.
* Call your saving `current_savings` which will start from `0`.
* Assume that you are not only saving your salary but also you are investing your savings on several companies which leads to 12% return each year. However, the interest affects your savings monthly. Each month, you receive an additional money income from your interest which equals to 1% of your savings. 
So, call the interest rate `interest_rate`.
* Call your monthly salary `monthly_salary`.
* You will save and invest some percentage of your monthly salary which we will call `percentage_saved`.

**Write a program that calculates how many months it will take to save the total cost of your dream car. Your program should ask the user to enter the following variables:**

* Monthly salary (`montly_salary`)
* Percentage saved (`percentage_saved`)
* The total cost of the car (`total_cost`)

### Hints

Here is an outline for you to start:

* Ask the user for the inputs.
* Initialize the variables.
* Calculate how many months it will take to buy the dream car.
* Print out what you found.

### Example Case

>>>   
Enter your monthly salary: 9500  
Enter the percentage to save, as a decimal: .15  
Enter the cost of the dream car: 300000   
Number of months: **114**   
>>>   


## PART B. A new model that is more expensive

In this part, again you will calculate the same thing with a small difference. In this part, every 12 months, a new model of your dream car is introduced which is more expensive than the one introduced a year ago. Every 12 months, the car's price increases. You will ask the same inputs with one additional which is the amount of the increase in the car's price and you will calculate the same output as in the PART A.

Write a program that calculates how many months it will take to save the total cost of your dream car. Your program should ask the user to enter the following variables:   

* Monthly salary (`monthly_salary`)
* Percentage saved (`percentage_saved`)
* The total cost of the car (`total_cost`)
* The percentage increase in the car's price (`percentage_increase`)

### Example case

>>>   
Enter your monthly salary: 9500    
Enter the percentage to save, as a decimal: .15    
Enter the cost of the dream car: 300000    
Enter the increase in the car's price, as a decimal: .08    
Number of months: **226**   
>>>    



## PART C. Good news: Salary raise!

In this part, again you will calculate the same thing with a small difference. Every 6 months, your monthly salary will  increase. For example, at the start, assume that your salary is 5000$ and with 5% increase every 6 months, your salary will become 5250$ at the beginning of the 7th month and it will become 5512.5$ at the beginning of the next year (13th month). You will ask the same inputs in Part B with one additional
which is the percentage salary raise and you will calculate the same output as in the PART A and PART B.

Write a program that calculates how many months it will take to save the total cost of your dream car. Your program should ask the user to enter the following variables:   

* Monthly salary (`monthly_salary`)   
* Percentage saved (`percentage_saved`)   
* The total cost of the car (`total_cost`)
* The percentage increase in the car's price (`percentage_car_increase`)
* The percentage salary raise of your monthly salary (`percentage_salary_increase`)

### Example case

>>>   
Enter your monthly salary: 9500   
Enter the percentage to save, as a decimal: .15   
Enter the cost of the dream car: 300000   
Enter the increase in the car's price, as a decimal: .08   
Enter the percentage salary raise, as a decimal: .12   
Number of months: **95**    
>>>

## PART D. The fastest way to save for the car

In this part, we will explore the bisection search which is an efficient search method. In the first three parts, you found out about the effects of the raises in your salary and the model introductions. Now, you need to find how much you need to save each month to be able to buy the car in 2 years (24 months). What is the percentage of the salary you need to save to achieve this? 

You will write a program that calculates the percentage of the monthly salary you need to save each month to buy your dream car. You **must** use the bisection search for this. 

Your program should ask the user for the following inputs:   

* Monthly salary (`monthly_salary`)
* The total cost of the car (`total_cost`)
* The percentage increase in the car's price (`percentage_car_increase`)
* The percentage salary raise of your monthly salary (`percentage_salary_increase`)

It should output the "Best saving rate" and "The number of steps in bisection search". 

### Hints

* Since hitting an exact value of the car will be difficult, we simply want your total savings at the end of 2 years be within 1000$ of the cost of the car.    

* You need to count the steps in bisection search because it is needed in the output.    

* We do not want you to worry about the difference between float values, for example, between 3.081% and 3.079%. Therefore, we can search for an integer value between 0 and 10000 and then convert it to a decimal percentage using simple float division. By searching this range, we simply limit the number of possibilities and we prevent the infinite loops caused by the infinite number of values between 0 and 1. The reason we use 0 to 10000 is to account for two additional decimal places in the range 0% and 100%. Your code should print out a decimal: for example, 0.030 for 3.08%.     

* In the cases where it is not possible to save with the current salary and the cost of the car, you should notify the user that it is not possible to save for this car in 24 months. 


**Note: Since there are multiple ways to implement bisection search, the number of steps in the output may not match perfectly with the example cases.**   

### Example cases

>>>   
Enter your monthly salary: 9500    
Enter the cost of the dream car: 200000    
Enter the increase in the car's price, as a decimal: .08    
Enter the percentage salary raise, as a decimal: .12   
The best saving rate: **0.793**      
The number of steps in bisection search: **7**   
>>>   
    

>>>   
Enter your monthly salary: 9500    
Enter the cost of the dream car: 300000    
Enter the increase in the car's price, as a decimal: .08    
Enter the percentage salary raise, as a decimal: .12    
**It is not possible to buy the car in two years**
>>>    

---

We provide some example test cases whose results will appear on GitHub actions after you commit your work. You can do multiple commits, only the latest one before the deadline will be graded. Note that there will be additional test cases that we will use when grading your solutions, so the points you see when you commit will not be your final grade.
