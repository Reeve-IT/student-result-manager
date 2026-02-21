students =[]

#basic work flow
while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Exit")
    
    choice=input("Enter your choice:")
    
    if choice=="1":
        print("Add Student selected")
        
        #stdent data
        name=input("Enter the name of the student:")
        s1=int(input("Enter Math marks:"))
        s2=int(input("Enter Java marks:"))
        s3=int(input("Enter Python marks:"))

        total=s1+s2+s3
        print("Total Marks out of 300=",total)
        
        #percentage calculation
        # percentage=total/3
        # print(percentage)
        maxixum_marks=300
        percentage=(total/maxixum_marks)*100
        print("Percentage=",percentage,"%")
        
        #grade assigning
        if percentage >=75:
            print("Grade 'A'")
        elif percentage <75:
            print("Grade 'B'")
        elif percentage <60:
            print("Grade 'C'")
        elif percentage <40:
            print("Fail")
        else:
            print("Error")
    
    elif choice=="2":
        print("view Student selected")
    elif choice=="3":
        break
    else:
        print("Invalid choice")
        
