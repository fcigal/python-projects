print("""********************************
Welcome to Cash Machine

Transactions:

1. Financial Status

2. Deposit Money

3. Withdraw Money

Press 'q' to exit the program.

********************************
     
      """)
financial_status = 1000

while True:
    process = input('Select the action you want to do:')
    
    if (process == 'q'):
        print('We wish you a nice day.')
        break
    elif (process == "1"):
        print(f"Your money status is ${financial_status}")
    elif (process == "2"):
        quantity = int(input('Enter amount: '))
        financial_status += quantity
        print(f'Your new balance is ${financial_status}')
    elif (process == '3'):
        quantity = int(input('Enter amount: '))
        if(quantity > financial_status):
            print('Insufficient balance!!')
            continue
        
        financial_status -= quantity
        print(f'Your remaining balance is ${financial_status}')      
    else:
        print('You used an invalid character')
        continue
    
