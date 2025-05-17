def inventory_stockmanagement():
    print("Stock Management")
    print(" 1. Maida")
    print(" 2. Sugar")
    print(" 3. Wheat Flour")
    print(" 4. Badam")
    print(" 5. Exit")

def stock_management():
    # Initialize stock variables
    maida = 0
    sugar = 0
    wheat_flour = 0
    badam = 0

    while True:
        inventory_stockmanagement()
        choice = input("Select the Items from the Menu (or enter 5 to exit) :")

        if choice == '5':
            break

        if choice == '1':
            maida = int(input("Enter the Number of Maida Bags :"))
        elif choice == '2':
            sugar = int(input("Enter the Number of Sugar Bags :"))
        elif choice == '3':
            wheat_flour = int(input("Enter the Number of Wheat Flour Bags :"))
        elif choice == '4':
            badam = int(input("Enter the Number of Badam Packets :"))
        else:
            print("Invalid Choice !!!")
        
        # Display stock after selection
        stock(maida, sugar, wheat_flour, badam)

def stock(maida, sugar, wheat_flour, badam):
    print("\nCurrent Stock:")
    print(f"Maida Bags       : {maida}")
    print(f"Sugar Bags       : {sugar}")
    print(f"Wheat Flour Bags : {wheat_flour}")
    print(f"Badam Packets    : {badam}")
    
# Run the stock management function
stock_management()
