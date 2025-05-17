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
        choice_1=input("Select a Savouries from the Menu (or enter 6 to exit) :")
        if choice_1 == '6':
            break
        try:
            quantity = int(input("Enter the Quantity in grams : "))
        except ValueError:
            print("Invalid Quantity !!!, please Enter a Number !!!")
            continue
        if choice_1 == '1':
            total_cost += 17 * quantity/50
            print(choice_1,quantity)
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
    print("Your total  bill for Savouries alone:", total_cost)
    
if __name__ == "__main__":
    takeorder_Savouries()
    
        