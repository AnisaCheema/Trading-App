#This program reflects the transaction in a trading application.The name of the Application is "Your stocks"

import datetime
print("\t\t\t\t\"Your Stocks\"\n\nPlease enter your username and date of birth for further processing.\n\n")
while True:
  customer_name = input("User Name:\t\t\t\t\t")
  isValidname=False
  if (customer_name.isalpha()== True):
    isValidname= True
    break
  else:
    print("sorry please enter only alphabets.numbers and symbols are not accepted.")
    continue
while True:
  customer_birthdate = input("Date of birth (D/M/Y):\t\t")
  day,month,year= customer_birthdate.split('/')
  customer_birthdate = True
  try:
    datetime.date(int(year),int(month),int(day))    
  except ValueError:
    birthdate = False
  if(customer_birthdate):
    break
  else:
    print ("The date of birth is not valid !")
    continue


print("\n\nWelcome to Your Stocks App Dear",customer_name,"!""\n\n")

deposit_money=int(input("How much amount do you want to deposit:\t\t€")) 
withdrawn_money=int(input("How much amount do you want to withdraw?\t€"))
current_status= deposit_money - withdrawn_money
existing_stocks = "Microsoft\t€217\n Amazon\t\t€2930\n Apple\t\t€110\n NVDIA\t\t€627\n LHA\t\t€11"

print("\n\nThank you Dear",customer_name,".""Please read the instructions below carefully and choose your desired function accordingly.\n\n")
print("1.  To check the status of your recent deposit,enter:\t\t\t\t\t\t\t1")
print("2.  To check your withdrawl money,enter:\t\t\t\t\t\t\t\t2")
print("3.  To check current status of your account,enter:\t\t\t\t\t\t\t\t\t\t3")
print("4.  To check the value of existing stocks,enter:\t\t\t\t\t\t4")

choice_of_user = input("\nEnter a number to call your desired function: ") 
if choice_of_user=="1":
  print(f"\n\nYou have recieved:","€",deposit_money)
elif choice_of_user=="2":
  print(f"\n\nYou have withdrawn:","€",withdrawn_money,"\n\n""Note:\tIf you withdraw any amount without any existing funds in your account,it will be considered as a loan.\nThis loan will be deducted on your next deposite of money.")
elif choice_of_user=="3":
  print(f"\n\nCurrent status of your account is:","€",current_status)
elif choice_of_user=="4":
  print("\n",existing_stocks)
else:
  print("Please choose the right option")

contact_data = "\n\nIf you have any questions,please contact us per email on abc@cmail.com, or\nCall our service center on 00123 456 789\nThank you for your trust in Your Stocks."
print(contact_data)