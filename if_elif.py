company=str(input("enter a comany name:")).lower()
langauge=str(input("enter a langauge name:")).lower()
experience=str(input("enter a experience fresher or 1 year experience:")).lower()
location=str(input("enter a location name:")).lower()

if company=="tcs" and langauge=="java" and experience=="fresher" and location=="chennai":
    print("you are eligible for tcs company")
elif company=="infosys" and langauge=="python" and (experience=="1 year experience" or  experience=="1") and location=="chennai": 
    print("you are eligible for infosys company") 
elif company=="wipro" and langauge=="python" and experience=="fresher" and location=="coimbatore":
    print("you are eligible for wipro company") 
elif company=="cognizant" and langauge=="java"  and (experience=="1 year experience" or  experience=="1")  and location=="bangalore":
  print("you are eligible for cognizant company")  
    
else: print("you are not eligible for any company")