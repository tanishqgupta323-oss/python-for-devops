import sys 
type =sys.argv[1]
if type == "t2.micro":
    print("ok,we will create the instant for you")
elif type == "t2.medium":
    print("it will charge 4 dollar a day")
elif type == "t2.large":
    print("it will charge 8 dollar a day")

else:
    print("give a valid instance type, so we can not create the instant for you")  
