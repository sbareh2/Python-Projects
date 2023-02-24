#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = float(input('What is your bill total? '))
personnum = float(input('How many people is there? '))
tip = float(input('what percentage would you like to pay in tip? '))
tip = 1 + (tip/100)
perperson = (total / personnum) * tip

print(f'Each person should pay {perperson:.2f}')
