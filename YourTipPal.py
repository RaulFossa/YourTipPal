#YourTipPal
#YourTipPal is a simple application that allows you to calculate the tip or gratuity!
#NOTE: "Please be nice to your server"
#raul_andres 12.14.2015


def thankyou():
    print("Thank you for using YourTipPal! \n\n\n\n\n")
    print("YourTipPal v1.0 12.14.2015")
def main():
    thankyou()

print("Welcome to YourTipPal! \n")

bill_amount = float(input("What is your total bill? $"))
x = 0
while bill_amount <= 0: #ERROR if 0 or a negative is entered
    print("That is NOT a valid entry! Try again")
    x += 1
    bill_amount = float(input("What is your total bill? $"))

print("Your bill amount is $",bill_amount," Dollars \n")

tip = int(input("Do you want to add 10%, 15%, 18% or 20% for your server? "))
print(" ")

if tip == 10 :
    add_tip = bill_amount * .10
    total_plus_tip = bill_amount + add_tip
    print("For a 10% Tip please add $", "%.2f" % add_tip,"\n")
    print("This will give you a total of $", "%.2f" % total_plus_tip,"\n") 
    #Output formated for 2 decimal places

if tip == 15 :
    add_tip = bill_amount * .15
    total_plus_tip = bill_amount + add_tip
    print("For a 15% Tip please add $", "%.2f" % add_tip,"\n")
    print("This will give you a total of $", "%.2f" % total_plus_tip,"\n")


if tip == 18 :
    add_tip = bill_amount * .18
    total_plus_tip = bill_amount + add_tip
    print("For a 18% Tip please add $", "%.2f" % add_tip,"\n")
    print("This will give you a total of $", "%.2f" % total_plus_tip,"\n")

if tip == 20 :
    add_tip = bill_amount * .20
    total_plus_tip = bill_amount + add_tip
    print("For a 20% Tip please add $", "%.2f" % add_tip,"\n")
    print("This will give you a total of $", "%.2f" % total_plus_tip,"\n")





main()