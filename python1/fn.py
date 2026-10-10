# develop a python program using functions to stimulate a simple atm banking system.and provide t
# the program should maintain an and initial account balance of 5000 and provide the followingb options through a menu:
#  1.check balance -display the current acount balance
#  2. deposit money- accept an amount from the user and add it to the balance
#  3. withdraw money- accept an amoount and withdraw it only if sufficient balance is avialable . otherwise display "insufficient balance."
#  4. EXIT- exit the atm system.

  



def check_balance(balance):
    print("current balance=*",balance)

def deposit(balance , amount):
    balance = balance + amount
    return balance

def withdraw(balance, amount):
    if amount<= balance:
        balance = balance-amount
        return balance
    else:
        print("insufficient balance")
        return balance
balance = 5000

while True:
 print("\n---ATM MENU---")
 print("1. check balance")
 print("2. deposit")
 print("3. withdraw")
 print("4. exit ")


 


