name          =      input("Enter the Name of the Customer          : ")  # getting name
phn_no_1      = int (input("Enter the Phone Number - 1              : ")) # getting customer phone number - 1
phn_no_2      = int (input("Enter the Phone Number - 2              : ")) # getting customer phone number -2
address       =      input("Enter the Address of the Customer       : ")  # getting Address of the customer 
date_of_order =      input("Enter the Date of order                 : ")  # getting the date of order
delivery_date =      input("Enter the Date of goods to be delivered : ")  # getting the date of delivery
delivery_time =      input("Enter the Delivery Time                 : ")  #getting the time of delivery
print("\n")
#order for sweet
total_cost_Sweet=''   #dummy variable outside the function
def display_Sweet():
    print("Sweet Menu")  # displaying the menu of sweets
    print(" 1. Laddu - Rs. 19")
    print(" 2. Jalebi - Rs. 19")
    print(" 3. Ice Barfi - Rs. 21")
    print(" 4. KDM Barfi - Rs. 21")
    print(" 5. Exit")
def takeorder_sweet():
    global total_cost_Sweet   #variable is declared as global to access outside the function
    total_cost_Sweet=0        #initial value
    while True:
        display_Sweet()
        choice=input("Select a Sweet from the Menu (or enter 5 to exit) :")
        if choice == '5':      #to break the loop if choice is 5
            break
        try:
            quantity = int(input("Enter the Quantity : "))   #to enter the quantity
        except ValueError:
            print("Invalid Quantity !!!, please Enter a Number !!!")   #print if the input is not a number
            continue   #continues the loop when we enter 1,2,3,4
        if choice =='1':
            total_cost_Sweet += 19 * quantity
        elif choice == '2':
            total_cost_Sweet += 19 * quantity
        elif choice == '3':
            total_cost_Sweet += 21 * quantity
        elif choice == '4':
            total_cost_Sweet += 21 * quantity
        else:
            print("Invalid Choice !!!")
    print("Your total Amount for Sweet alone:", total_cost_Sweet)   #returns the total amount of sweet
    
takeorder_sweet()   #calling the function
            
print("\n")
#order for savouries
total_cost= ''     #dummy variable outside the function
def display_Savouries():
    print("Savouries Menu")   # displaying the menu of savouries
    print(" 1. Mixture - 50g Rs. 17")
    print(" 2. Kara Sev - 50g Rs. 17")
    print(" 3. Butter Sev - 50g Rs. 18")
    print(" 4. Big Muruku - Rs. 19")
    print(" 5. Small Muruku - Rs. 9")
    print(" 6. Exit")
def takeorder_Savouries():
    global total_cost     #variable is declared as global to access outside the function
    total_cost=0          #initial value
    while True:
        display_Savouries()
        choice_1=input("Select a Savouries from the Menu (or enter 6 to exit) :")
        if choice_1 == '6':        #to break the loop if choice is 6
            break
        try:
            quantity = int(input("Enter the Quantity in grams : "))    #to enter the quantity in grams
        except ValueError:
            print("Invalid Quantity !!!, please Enter a Number !!!")    #print if the input is not a number
            continue        #continues the loop when we enter 1,2,3,4,5
        if choice_1 == '1':
            total_cost += 17 * quantity/50
        elif choice_1 == '2':
            total_cost += 17 * quantity/50
        elif choice_1 == '3':
            total_cost += 18 * quantity/50
        elif choice_1 == '4':
            total_cost += 19 * quantity
        elif choice_1 == '5':
            total_cost += 9 * quantity
        else:
            print("Invalid Choice !!!")
    print("Your total  Amount for Savouries alone:", total_cost)       #returns the total amount of savouries
takeorder_Savouries()     #calling the function
        
print("\n")   #to leave a sinle empty line
#Total 
whole_amount=total_cost_Sweet+total_cost   #calculation of whole amount(sweet and savouries)
print("Total Amount for both Sweets and Savouries is :",whole_amount)   #to print whole amount
paid=int(input("Enter the Amount to pay in advance            : "))     #amount to pay in advance
balance=whole_amount-paid     #calculation for balance amount to be paid
print("Paid Amount is                                : ",paid)       #paid amount
print("Balance amount to be paid is                  : ",balance)     #balance amount to be paid
#payment type
payment_type = input("Payment type (Cash/UPI/Card)?                 : ")    #payment type
#Door Delivery
ch = 'yes'
while ch.lower() == "yes":
   print("Door Delivery \n1.Yes\n2.No") #to display the options
   choice = input("Enter choice(1/2):") #to enter the choice
   if choice == '1':
      dd_address=input("Enter the Address of Delivery :")  #to enter the address of the delivery
      break 
   elif choice == '2':   #if choice is 2 then the statement is break
      break
   else:
      print("Invalid input")  #if any invalid option entered
   if ch== "no":
      break
print("\n")
# below lines are for reading purpose
print("ORDER SUCCESSFUL !!!!. ORDER DETAILS !!!")
print("Customer Name           : ", name)
print("Phone Number - 1        : ", phn_no_1)
print("Phone Number - 2        : ", phn_no_2)
print("Customer Address        : ", address)
print("Date of Order           : ", date_of_order)
print("Date of Delivery        : ", delivery_date)
print("Delivery Time           : ", delivery_time)
print("Total cost of Sweet     : ", total_cost_Sweet)
print("Total cost of Savouries : ", total_cost)
print("Total Amount            : ", whole_amount)
print("Balance                 : ", balance)
print("Amount paid in Advance  : ",paid)
print("Payment Type            : ", payment_type)
print("Door Delivery           : ", ch)
print("Door Delivery Address   : ", dd_address)

