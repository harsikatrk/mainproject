name =input("Enter the Name of the Customer : ") # getting name
phn_no_1 = int (input("Enter the Phone Number - 1 : ")) # getting customer phone number - 1
phn_no_2 = int (input("Enter the Phone Number - 2 : ")) # getting customer phone number -2
address = input("Enter the Address of the Customer : ") # getting Address of the customer 
date_of_order = int(input("Enter the date of order : "))  # getting the date of order
delivery_date = int(input("Enter the date of goods to be delivered : ")) # getting the date of delivery
#order for sweet
def display_Sweet():
    print("Sweet Menu")
    print(" 1. Laddu - Rs. 20")
    print(" 2. Jalebi - Rs. 20")
    print(" 3. Ice Barfi - Rs. 16")
    print(" 4. KDM Barfi - Rs. 16")
    print(" 5. Exit")
def takeorder_sweet():
    total_cost_Sweet=0
    while True:
        display_Sweet()
        choice=input("Select a Sweet from the Menu (or enter 5 to exit) :")
        if choice == '5':
            break
        try:
            quantity = int(input("Enter the Quantity : "))
        except ValueError:
            print("Invalid Quantity !!!, please Enter a Number !!!")
            continue
        if choice =='1':
            total_cost_Sweet += 20 * quantity
        elif choice == '2':
            total_cost_Sweet += 20 * quantity
        elif choice == '3':
            total_cost_Sweet += 16 * quantity
        elif choice == '4':
            total_cost_Sweet += 16 * quantity
        else:
            print("Invalid Choice !!!")
    print("Your total bill for Sweet alone:", total_cost_Sweet)
if __name__ == "__main__":
    print("Welcome to Sweet Shop!")
    takeorder_sweet()
            
print("\n")
#order for savouries
def display_Savouries():
    print("Savouries Menu")
    print(" 1. Mixture - 50g Rs. 17")
    print(" 2. Kara Sev - 50g Rs. 17")
    print(" 3. Butter Sev - 50g Rs. 18")
    print(" 4. Big Muruku - Rs. 19")
    print(" 5. Small Muruku - Rs. 9")
    print(" 6. Exit")
def takeorder_Savouries():
    total_cost=0
    while True:
        display_Savouries()
        choice=input("Select a Savouries from the Menu (or enter 6 to exit) :")
        if choice == '6':
            break
        try:
            quantity = int(input("Enter the Quantity in grams : "))
        except ValueError:
            print("Invalid Quantity !!!, please Enter a Number !!!")
            continue
        if choice == '1':
            total_cost += 17 * quantity/50
        elif choice == '2':
            total_cost += 17 * quantity/50
        elif choice == '3':
            total_cost += 18 * quantity/50
        elif choice == '4':
            total_cost += 19 * quantity
        elif choice == '5':
            total_cost += 9 * quantity
        else:
            print("Invalid Choice !!!")
    print("Your total  bill for Savouries alone:", total_cost)
if __name__ == "__main__":
    takeorder_Savouries()
        
print("\n")
#Total 
whole_amount=int(input("Enter the total amount to be paid : "))
paid=int(input("Enter the Amount to pay in advance : "))
balance=whole_amount-paid
print("Paid Amount is : ",paid)
print("Balance amount to be paid is : ",balance)
#payment type
payment_type = input("Payment type (Cash/UPI/Card)? : ")
#Door Delivery
ch = "yes"
while ch.lower() == "yes":
   print("Door Delivery \n1.Yes\n2.No") #to display the options
   choice = input("Enter choice(1/2):") #to enter the choice
   if choice == '1':
      dd_address=input("Enter the Address of Delivery :")
      break #to print the addition operator
   elif choice == '2':
      break
   else:
      print("Invalid input")
   if ch== "no":
      break
print("\n")
# below lines are for reading purpose
print("Customer Name : ",name)
print("Phone Number - 1 : ",phn_no_1)
print("Phone Number - 2 : ",phn_no_2)
print ("Customer Address",address)
print("Date of Order : ",date_of_order)
print("Date of Delivery : ",delivery_date)
#print("Total cost of Sweet : ",total_cost_Sweet)
#print("Total cost of Savouries : ",total_cost_Sweet)
print("Total Amount",whole_amount)
print("Door Delivery : ",ch)
print("Delivery Address : ",dd_address)
print("Balance : ",balance)
print ("Amount paid in Advance : ",paid)
print("Payment Type : ",payment_type)
