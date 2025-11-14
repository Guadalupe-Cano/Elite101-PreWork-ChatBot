from Bank_User_Info import userInfo
import random 

print("Welcome to Elite101 Bank")

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
user_age = int(input("Pleasure to meet you " + first_name + "! How old are you? "))
print("Welcome! How can I assist you today?") 
print(" ")
print("1. Account management ")
print("2. About our Bank")
print("3. Support and security ")
print("4. Exit conversation/ no more questions! ") 




user_options = int(input("Enter an option number: "))

print(" ")
      

if user_options == 1:
  print("Account management")
  print("1. Check balances")
  print("2. Manage cards")
  print("3. Create Bank Account")

  account_user_options = int(input("What do you specifically need assistance for?(enter number) ")) 

  if account_user_options == 1:
    print(" ")
    print("Login into account by checking for ID!")
    print("In order to log into your account you need to know your account ID. ")
    account_ID_Inputs = int(input("What is your account ID: "))
    for bankUsers in userInfo:
      if bankUsers["AccountID"] == account_ID_Inputs:
        print("Hello " + bankUsers["name"])
        print("Balance: " + str(bankUsers["CheckBalance"]))


  if account_user_options == 2:
    print("Login into account by checking for ID!")
    print("In order to log into your account you need to know your account ID. ")
    account_ID_Inputs = int(input("What is your account ID: "))
    for bankUsers in userInfo:
      if bankUsers["AccountID"] == account_ID_Inputs:
        print("Hello " + bankUsers["name"])
        print("Cards: " + bankUsers["CardType"])
        changeCardType = input("Would you like to change card type? ")
        if changeCardType.lower() == "yes":
          if bankUsers["CardType"].lower() == "credit":
            bankUsers["CardType"] == "Debit"
          if bankUsers["CardType"].lower() == "Debit":
            bankUsers["CardType"] == "Credit"
          print("Card Successfully changed!")
        if changeCardType.lower() == "no":
          print("Okay! Have a great Day!")


  if account_user_options == 3:
    print(" ")
    print("Time to create your account!")
    if user_age >18:
      print("Hello " + first_name +"! Since you are over 18 you can create:")
      print("1-Individual Accounts\n2-Checking Accounts\n3-savings Accounts")
      account_choice = int(input("What type of account would you like(enter a number): "))
      user_cardType = input("What type of card would you like? ")
      print(" ")
      checkBalance_insert = int(input("Insert balance: "))
      randomizedNum =  random.randint(10000000, 99999999)
      print("Your ID login number: " + str(randomizedNum))
      userInfo.append({"name": (first_name + " " + last_name), "age": user_age, "AccountType": account_choice, "AccountID": randomizedNum, "CheckBalance": checkBalance_insert, "CardType": user_cardType })  
      print("Your account has been successfully added! ")
    if user_age<18:
      print(" Hello " + first_name +"! Since you are a minor you can only create a joint account. ")
      print("A minor legally not allowed to create an account. Please have your gaurdian create an joint account for you!")
  
elif user_options == 2:
  print("About our bank!")
  print("What would you like to see information about: ")
  print(" ")
  print("1-Age requirments\n2-Types of accounts\n3-Types of cards\n4-Tips for checking balances, transferring funds, paying bills, and managing accounts.")
  bankInfoNum = int(input("Enter a number: "))
  print(" ")
  if bankInfoNum == 1:
    print("18 years old → Minimum age to open a bank account on your own in most of the U.S.\nUnder 18 (minors) → Cannot open accounts alone; need a parent/guardian as co-owner or custodian\nTeen accounts (13–17 years old) → Many banks offer special accounts with parental consent; teens can deposit, withdraw, and use debit cards\nChildren under 13 → Usually limited to custodial accounts managed entirely by parents/guardians\nLegal contracts → The age of majority (18) is when contracts become binding; minors’ contracts are typically voidable unless state law provides exceptions.")
    print(" ")
  elif bankInfoNum == 2:
    print("Checking Account → For everyday spending, bill payments, debit card use, unlimited transactions\nSavings Account → For storing money safely, earns interest, limited monthly withdrawals\nRetirement Accounts (IRA/401k) → Long-term savings with tax benefits, restricted access until retirement age\nCustodial/Minor Accounts → Managed by parent/guardian until child reaches legal age\nBusiness Accounts → Designed for companies, includes checking, savings, and merchant services. ")
    print(" ")
  elif bankInfoNum == 3:
    print("Debit Card → Linked directly to your checking account; spend only what you have.\nCredit Card → Borrow money up to a limit; repay later with interest if not paid in full.\nBusiness Card → Designed for companies; helps track expenses separately from personal accounts. ")
    print(" ")
  elif bankInfoNum == 4:
    print("Checking balances → Log in weekly, set low-balance alerts, and reconcile with statements.\nTransferring funds → Use scheduled transfers for savings, double-check recipient details, and avoid public Wi-Fi.\nPaying bills → Set up auto-pay for recurring bills, track due dates, and confirm payments cleared.\nManaging accounts → Review fees, enable two-factor authentication, and use budgeting tools to monitor spending.")
    print(" ")

  

elif user_options == 3:
  print("Support and security")
  print("1. Update information")
  print("First let us login! ")
  account_ID_Inputs = int(input("What is your account ID: "))
  for bankUsers in userInfo:
    if bankUsers["AccountID"] == account_ID_Inputs:
        print("Hello " + bankUsers["name"])
        print("Balance: " + str(bankUsers["CheckBalance"]))
        insert_or_withdraw = input("Would you like to insert money or with draw? (type: 'insert' or 'withdraw') ")
        if insert_or_withdraw.lower() == "insert":
          userInsert = int(input("How much money would you like to insert: "))
          bankUsers["CheckBalance"] += userInsert
          print("$" +str(userInsert) +" has been added into your checking balance. ")
          print("New Balance: " + str(bankUsers["CheckBalance"]) + ".")
        if insert_or_withdraw.lower() == "withdraw":
          userWithdraw = int(input("How much money would you like to withdraw: "))
          bankUsers["CheckBalance"] -= userWithdraw
          print("$" +str(userWithdraw) +" has been removed from your checking balance. ")
          print("New Balance: " + str(bankUsers["CheckBalance"]) + ".")
          

elif user_options == 4:
  print("Have a great Day!")

else:
  print("Invalid! Try again")






