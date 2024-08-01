#Write python script to  print a mcqs question if answer is correct or and whether user given is valid or not,.

print("Q1: Which one of the following is assignment operator?")
print("(a) +")
print("(b) -")
print("(c) =")
print("(d) ==")

answer = input("Enter your answer: ")

if answer == "a" or answer == "b" or answer == "c" or answer == "d":
    if(answer == "c"):
        print("Your answer is correct")
    else:
        print("Your answer is incorrect")
else:
    print("Invalid Input")