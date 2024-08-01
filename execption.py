


a = 5 
try:
    age = int(input("Enter your age:"))
    if age > 7:
        print("you are eligible to play game")
    else:
        print("you are not eligible to play game")
except:
    print("Invalid Input")
finally:
    print("Thank you for using our software")