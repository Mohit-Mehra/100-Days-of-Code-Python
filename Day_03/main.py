print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are ₹50")
        bill = 50
    elif age <= 18:
        print("Youth tickets are ₹70")
        bill = 70
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on Us!")
    else:
        print("Adult tickets are ₹100")
        bill = 100

    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        # Add ₹30 to thier bill
        bill += 30
    print(f"Your final bill is {bill}")
else:
    print("You cannot ride the rollercoaster!")
