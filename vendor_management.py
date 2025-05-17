def vendor_management():
    print("Items")  
    print(" 1. Maida ")
    print(" 2. Sugar ")
    print(" 3. Milk ")
    print(" 4. Nuts ")
    print(" 5. Wheat Flour ")
    print(" 6. Groceries ")
    print(" 7. Exit ")
def vendor_details():      
    while True:
        vendor_management()
        choice=input("Select the Raw Materials to Display the details of Vendors : ")
        if choice == '7':      
            break
        
        var_1 = {
                 'Name' : "xxx", 
                 'Products' : "Maida", 
                 'Phone Number': 9876543210, 
                 'Address': "aaa, Madurai",
                 'Email-Id': "xxx@gmail.com"
                }
        var_2 = {
                 'Name' : "yyy", 
                 'Products' : "Sugar", 
                 'Phone Number': 8872343210, 
                 'Address': "yyy, Madurai",
                 'Email-Id': "yyy@gmail.com"
                 }
        var_3 = {
                 'Name' : "zzz", 
                 'Products' : "Milk", 
                 'Phone Number': 8934670771, 
                 'Address': "zzz, Madurai",
                 'Email-Id': "zzz@gmail.com"
                 }
        var_4 = {
                 'Name' : "kkk", 
                 'Products' : "Nuts", 
                 'Phone Number': 83347713490, 
                 'Address': "kkk, Madurai",
                 'Email-Id': "kkk@gmail.com"
                 }
        var_5 = {
                 'Name' : "mmm", 
                 'Products' : "Wheat Flour", 
                 'Phone Number': 9786541234, 
                 'Address': "mmm, Madurai",
                 'Email-Id': "mmm@gmail.com"
                 }
        var_6 = {
                 'Name' : "nnn", 
                 'Products' : "Groceries", 
                 'Phone Number': 856709114, 
                 'Address': "nnn, Madurai",
                 'Email-Id': "nnn@gmail.com"
                 }
        if choice =='1':
            print(var_1)
        elif choice == '2':
            print(var_2)
        elif choice == '3':
           print(var_3)
        elif choice == '4':
            print(var_4)
        elif choice == '5':
            print(var_5)
        elif choice == '6':
            print(var_6)
        else:
            print("Invalid Choice !!!")
       
vendor_details()