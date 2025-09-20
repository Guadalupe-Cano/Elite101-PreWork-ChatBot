print("Welcome to Elite101 Chat Bot!")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
user_age = int(input("Pleasure to meet you " + first_name + "! How old are you? "))
print("WoW you're "+ str(user_age) +" years old! Welcome! How can I assist you today? ")
print(" ")
print("Please choose from the following options! ")
print("1. learn about AI ")
print("2. Environemental consequences of AI ")
print("3. What Can I do to minimize the effetcs of AI water thermal pollution ")
print("4. Benefits of AI ")
print("5. Misconceptions over AI ")
print("6. Exit conversation/ no more questions! ") 

user_options = int(input("Enter an option number: "))

if user_options == 1:
  print(" Info about AI")
  user_options = int(input("Have another questio! Enter an option number: "))
  
if user_options == 2:
  print(" Info about AI consequences")
  user_options = int(input("Have another questio! Enter an option number: "))
  
if user_options == 3:
  print(" Info about AI")
  user_options = int(input("Have another questio! Enter an option number: "))
  
if user_options == 4:
  print(" Positive Info About AI ")
  user_options = int(input("Have another questio! Enter an option number: "))
  
if user_options == 5:
  print(" Misconceptions over AI")
  user_options = int(input("Have another questio! Enter an option number: "))
  
if user_options == 6:
  print(" GoodBye " + first_name+ "! Hope you have a great day!")
    

else:
  print("Invalid! Try again")
  user_options = int(input("Enter an option number: "))






