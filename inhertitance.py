#inheritance ----------single Inheritance

# class atm:
#     def __init__(self,bank_name,location,balance=0):
#         self.bank_name = bank_name
#         self.location = location
#         self.balance = balance

# class card(atm):
#     def display_menu(self):
#         print("\nATM Menu:")
#         print("1.Credit")
#         print("2.Debit")
#         print("3.Balance enquiry")
#         print("4.Exit")
#     def choose_options(self):
#         return input("choose the options that displays on Menu (1-4): ")
#     def credit(self):
#         amount= int(input("enter your amount: "))
#         self.balance += amount
#         print(f"Rs:{amount} is credited to your account successfully:")
#     def debit(self):
#         amount=int(input("enter your amount: "))
#         self.balance -= amount
#         if amount >self.balance:
#             print("insufficient balance in your account: ")
#         else:
#             print(f"Rs:{amount} is debited from your account: ")
#     def balance_enquiry(self):
#         print(f"{self.balance}Rs is available in your account: " )
# bank=card("HDFC","Araku")
# print()
# print("WELCOME to our Branch, Have a Pleasent Day")
# print()
# bank.display_menu()
# while True:
#     option = bank.choose_options()
#     if option <= '0' or option >= '5':
#         print("Invalid option, please check and enter the correct option ")
#     elif option == '1':
#         bank.credit()
#     elif option == '2':
#         bank.debit()
#     elif option == '3':
#         bank.balance_enquiry()
#     else:
#         print("Thank you for Visiting ")
#         break
#   print()

#___________________________Multilevel Inheritance______________________#

# class ATM():
#     def __init__(self,bank,location,balance=0):
#         self.bank=bank
#         self.location=location
#         self.balance=balance
# class card(ATM):
#     def display_menu(self):
#         print("\nATM Menu:")
#         print('1.Credit')
#         print('2.Debit')
#         print('3.Balance enquiry')
#         print('4.Exit')
# class options(card):
#     def choose_options(self):
#         return input("select the option (1-4): ")
# class deposit(options):
#     def credit(self):
#         amount=int(input("enter your amount: "))
#         self.balance += amount
#         print(f"{amount}Rs credited to your account: ")
# class withdraw(deposit):
#     def debit(self):
#         amount=int(input("enter your amount: "))
#         self.balance-=amount
#         if amount > self.balance:
#             print("insufficient amount in your ")
#         else:
#             print(f"{amount}Rs debited from your account")    
# class final_bal(withdraw):
#     def balance_enquiry(self):
#         print(f"The available balance is Rs:{self.balance}")

# bank=final_bal("HDFC","Araku")
# print()
# print("WELCOME to our Branch, Have a Pleasent Day")
# print()
# bank.display_menu()
# while True:
#     option = bank.choose_options()
#     if option <= '0' or option >= '5':
#         print("Invalid option, please check and enter the correct option ")
#     elif option == '1':
#         bank.credit()
#     elif option == '2':
#         bank.debit()
#     elif option == '3':
#         bank.balance_enquiry()
#     else:
#         print("Thank you for Visiting ")
#         break
#         print()

#______________________________Hierarchical Inheritance______________________________#

# class ATM():
#     def __init__(self,bank_name,location,balance=0):
#         self.bank_name= bank_name
#         self.location= location
#         self.balance= balance
# class branch(ATM):
#     def display_menu(self):
#         print("\nATM Menu:")
#         print('1.Credit')
#         print('2.Debit')
#         print('3.Balance enquiry')
#         print('4.Exit')
# class options(ATM):
#     def choose_options(self):
#         return input("choose the correct options from menu (1-4): ")
#     def credit(self):
#         amount= int(input("enter your amount : "))
#         global balance
#         self.balance += amount
#         print(f"{amount}Rs is credited in your account: ")
#     def debit(self):
#         amount=int(input("enter your amount"))
#         global balance
#         self.balance -= amount
#         if amount > self.balance:
#             print("Insuffcient balance in your account ")
#         else:
#             print(f"{amount}Rs debited from your account ")
#     def balance_enquiry(self):
#         print(f"The available balance in your account is {self.balance}")

# bank = branch('HDFC','Vizag')
# print()
# print("WELCOME to our Bank, Have a Pleasent Day")
# print()
# bank.display_menu()
# bank_x = options('HDFC','Vizag')
# while True:
#     option = bank_x.choose_options()
#     if option <= '0' or option >= '5':
#         print("Invalid option, please check and enter the correct option ")
#     elif option == '1':
#         bank_x.credit()
#     elif option == '2':
#         bank_x.debit()
#     elif option == '3':
#         bank_x.balance_enquiry()
#     else:
#         print("Thank you for Visiting ")
#         break
#     print()


#________________________________MULTIPLE Inheritance_____________________________________#

# class ATM():
#     def __init__(self,bank_name,location,balance=0):
#         self.bank_name= bank_name
#         self.location= location
#         self.balance= balance
# class branch():
#     def display_menu(self):
#         print("\nATM Menu:")
#         print('1.Credit')
#         print('2.Debit')
#         print('3.Balance enquiry')
#         print('4.Exit')
# class options(ATM,branch):
#     def choose_options(self):
#         return input("choose the correct options from menu (1-4): ")
#     def credit(self):
#         amount= int(input("enter your amount : "))
#         global balance
#         self.balance += amount
#         print(f"{amount}Rs is credited in your account: ")
#     def debit(self):
#         amount=int(input("enter your amount"))
#         global balance
#         self.balance -= amount
#         if amount > self.balance:
#             print("Insuffcient balance in your account ")
#         else:
#             print(f"{amount}Rs debited from your account ")
#     def balance_enquiry(self):
#         print(f"The available balance in your account is {self.balance}")

# bank = options('HDFC','Vizag')
# print()
# print("WELCOME to our Bank, Have a Pleasent Day")
# print()
# bank.display_menu()
# while True:
#     option = bank.choose_options()
#     if option <= '0' or option >= '5':
#         print("Invalid option, please check and enter the correct option ")
#     elif option == '1':
#         bank.credit()
#     elif option == '2':
#         bank.debit()
#     elif option == '3':
#         bank.balance_enquiry()
#     else:
#         print("Thank you for Visiting ")
#         break
#     print()