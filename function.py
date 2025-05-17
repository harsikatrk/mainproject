class billing_payment():
    def billing_payment_1(self , cust_Name , phn_Num_1 , phn_Num_2 , Address ,date_Of_order , date_Of_delivery , delivery_Time , items , quantity , door_Delivery , total , advance , balance , payment_Type ):
        self.cust_Name = cust_Name
        self.phn_Num_1 = phn_Num_1
        self.phn_Num_2 = phn_Num_2
        self.Address = Address
        self.date_Of_order=date_Of_order
        self.date_Of_delivery = date_Of_delivery
        self.delivery_Time = delivery_Time
        self.items = items
        self.quantity = quantity
        self.door_Delivery = door_Delivery 
        self.total = total
        self.advance = advance
        self.balance = balance
        self.payment_Type = payment_Type
        cust_Name = input("Enter the Customer Name : ")
        phn_Num_1 = int(input("Enter the Customer Phone Number - 1 : "))
        phn_Num_2 = int(input("Enter the Customer Phone Number - 2 : "))
        Address = input("Enter the Customer Address : ")
        date_Of_order = int(input("Enter the Date of Order : "))
        date_Of_delivery = int(input("Enter the Date of Delivery : "))
        delivery_Time = int(input("Enter the Delivery Time : "))
        items = input("Enter the Items : ")
        quantity = int(input("Enter the Quantity : "))
        door_Delivery = input("Enter the address of door delivery : ")
        total = int(input("Enter the total amount : ")) 
        advance = int(input("Enter the advance to be paid : "))
        balance = int(input("Enter the balance to be paid : "))
        payment_Type = input("Enter the type of payment : ")
    cust = billing_payment_1()

    