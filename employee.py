employees = {
    "Arun": {"id": 101, "salary": 25000},
    "Priya": {"id": 102, "salary": 30000},
    "Karthik": {"id": 103, "salary": 28000},
    "Divya": {"id": 104, "salary": 35000},
    "Vikram": {"id": 105, "salary": 40000},
    "Sneha": {"id": 106, "salary": 27000},
    "Rahul": {"id": 107, "salary": 32000},
    "Meena": {"id": 108, "salary": 29000},
    "Suresh": {"id": 109, "salary": 36000},
    "Anitha": {"id": 110, "salary": 31000}
}

print("1.Add Employee")
print("2.Edit Employee")
print("3.Delete Employee")

choice=(input("Enter your choice : "))

if choice=="1":
    name=input("Enter Employee Name : ")
    
    if name in employees:
        print("Employee name already exist!")
    
    else:
        emp_id=int(input("Enter employee id :"))
        salary=float(input("Enter employee salary : "))
        employees[name]={"id" : emp_id,"salary" : salary}
        print("Employee Added Successfully!")

elif choice=="2":
    name=input("Enter employee name :")
    if name in employees:
        print("Press 1 for edit employee name:")
        print("press 2 for edit employee id")
        print("Press 3 for edit employee salary")
        print("press 4 if you want to edit full details :")
    
        option=int(input("Enter your Choice : "))
    
        if option==1:
            new_name=input("Enter Employee's new name : ")
            if new_name in employees:   
                print("Employee name already exist !")
        
                
            else :  
                employees[new_name]=employees[name]
                del employees[name]
                print("Name updated successfully !")
                   
            
        elif option==2:
            new_id=int(input("Enter new id : "))
            employees[name]["id"]=new_id
            print("ID updated Successfully!")
        
        elif option==3:
            sal=float(input("Enter new Salary : "))
            employees[name]["salary"]=sal
            print("Salary updated Successfully!")    
    
        elif option==4:
            n=input("Enter new name : ")
            if n in employees and n!=name :
                print("Employee already exist!")
                
            else:
                i=int(input("Enter new id : "))  
                s=float(input("Enter new salary : "))        
                del  employees[name]
                employees[n]={"id":i,"salary" :s}
                print("Employee details updated Successfully!")
        
elif choice=="3":
    na=input("Enter employee name : ")
    if na in employees:
        del employees[na]
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")    


else :
    print("Invalid Option")        