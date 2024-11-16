print("WELCOME TO KRISH ATM")
print("---------------------")

bal = 1000

while(True):
    print("---------------------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit\n")
    try:
        user_input = int(input("Choose an option: "))
        if user_input == 1 :
            
            
            print(f"Your balance is $ {bal}")
        elif user_input == 2:
            deposit = int(input("Enter the amount to be Deposited: "))
            if deposit < 0 :
                raise ValueError ("Enter the valid amount")
            bal+=deposit
            print(f"Amount Deposited! Your balance is $ {bal}")
        elif user_input == 3 :
            withdraw = int(input("Enter the amount to Withdraw: "))
            if withdraw > bal or withdraw < 0 :
                raise ValueError ("Enter the valid amount")
            bal-=withdraw
            print(f"Withdrawal Succussful! Your balance is $ {bal}")

        elif user_input == 4:
            print("Thank you Visit again!")
            break
        else :
            print("Invalid Option")
    except Exception as e :
        print("Choose from the given option. ",e)