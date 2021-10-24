print("""

Welcome Perfect Number Finder

      """)
 
number = int(input('Please Enter a Number: '))
sum = 0
i = 1
while (i < number):
    if number % i == 0:
        sum += i 
    i += 1 
if (sum == number):
    print(f'{number} is perfect number')
else:
    print(f'{number} is a not perfect number')      
