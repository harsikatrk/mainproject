class SweetStall:
    def __init__(self):
        # Inventory of sweets in the stall (name, price, quantity)
        self.inventory = {
            "Gulab Jamun": {"price": 20, "quantity": 50},
            "Rasgulla": {"price": 30, "quantity": 50},
            "Jalebi": {"price": 15, "quantity": 50},
            "Barfi": {"price": 40, "quantity": 50},
            "Ladoo": {"price": 25, "quantity": 50}
        }
        self.total_earnings = 0
    
    def display_inventory(self):
        print("Sweet Stall Inventory:")
        for sweet, details in self.inventory.items():
            print(f"{sweet} - Price: ₹{details['price']} | Quantity: {details['quantity']}")
    
    def sell_sweet(self):
        self.display_inventory()
        sweet_name = input("\nEnter the sweet you want to buy: ").capitalize()
        
        if sweet_name in self.inventory:
            quantity = int(input(f"How many {sweet_name} would you like to buy? "))
            if quantity <= self.inventory[sweet_name]["quantity"]:
                total_price = quantity * self.inventory[sweet_name]["price"]
                self.inventory[sweet_name]["quantity"] -= quantity
                self.total_earnings += total_price
                print(f"Total cost for {quantity} {sweet_name}(s) is ₹{total_price}.")
                print(f"Thank you for your purchase! You have bought {quantity} {sweet_name}(s).")
            else:
                print(f"Sorry, we don't have enough stock of {sweet_name}.")
        else:
            print(f"{sweet_name} is not available in the menu.")
    
    def restock_sweet(self):
        self.display_inventory()
        sweet_name = input("\nEnter the sweet you want to restock: ").capitalize()
        
        if sweet_name in self.inventory:
            quantity = int(input(f"How many {sweet_name} would you like to add to the stock? "))
            self.inventory[sweet_name]["quantity"] += quantity
            print(f"{sweet_name} has been restocked. New quantity: {self.inventory[sweet_name]['quantity']}")
        else:
            print(f"{sweet_name} is not available in the menu.")
    
    def view_earnings(self):
        print(f"\nTotal earnings so far: ₹{self.total_earnings}")

def main():
    stall = SweetStall()

    while True:
        print("\nWelcome to the Sweet Stall Management System!")
        print("1. View Inventory")
        print("2. Sell Sweets")
        print("3. Restock Sweets")
        print("4. View Earnings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            stall.display_inventory()
        elif choice == '2':
            stall.sell_sweet()
        elif choice == '3':
            stall.restock_sweet()
        elif choice == '4':
            stall.view_earnings()
        elif choice == '5':
            print("Thank you for using the Sweet Stall Management System!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
