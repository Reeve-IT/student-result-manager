students =[]

while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Exit")
    
    choice=input("Enter your choice:")
    
    if choice=="1":
        print("Add Student selected")
    elif choice=="2":
        print("view Student selected")
    elif choice=="3":
        break
    else:
        print("Invalid choice")
        
    