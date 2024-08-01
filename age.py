# write a python program to calulate age of perfrom where date of birth is a user input

#def age_calculator(current_year,birth_year):
    
 #   age = current_year - birth_year


  #  print("Your is age is",age, "years")

#age_calculator(2024,2000)

from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

try:
    # Get the user's date of birth
    dob_str = input("Enter your date of birth: ")
    
    # Convert the input string to a datetime object
    dob = datetime.strptime(dob_str, "%Y")
    
    # Calculate age
    age = calculate_age(dob)
    
    print("Your age is:", age)
except ValueError:
    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
