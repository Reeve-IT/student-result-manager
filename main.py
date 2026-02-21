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
        if total >300:
            print("Error!! check subject marks entered :(")
        else:
            print("Total Marks=",total,"/300")
            
             #percentage calculation
             # percentage=total/3
             # print(percentage)
            maxixum_marks=300
            percentage=(total/maxixum_marks)*100
            print("Percentage=",percentage,"%")
            
            #grade assigning
            if percentage >=75:
                 grade="A"
                        
            elif percentage >=60:
                grade="B"
            elif percentage >=40:
                grade="C"
            else:
                grade="Fail"
            print("Grade",grade)
           
    elif choice=="2":
        print("view Student selected")
    elif choice=="3":
        break
    else:
        print("Invalid choice")
        
