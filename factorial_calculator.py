print("""****************************
      
Welcome To Factorial Calculator
 
Press q To Exit

****************************""")
factorial = 1
while True:
    number = input('Number :')
    if (number == 'q'):
        print('Checking out...')
        break
    else:
        number = int(number)
        for i in range(2,number + 1):
            factorial *=i
        print(factorial) 
        break  
