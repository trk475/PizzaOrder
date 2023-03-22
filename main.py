print("Welcome to Rami's Pizza!")
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
bill = 0
size = input("What sie pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want to add Pepperoni? ? Y or N ")
add_extra_cheese = input("Do you want to add extra Cheese ? ? Y or N ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if add_extra_cheese == "Y":
    bill += 1
print(f" Your final bill is {bill}$ ")






















