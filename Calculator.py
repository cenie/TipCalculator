'''
Simple tip Calculator

Notes:

simple tip calculator
use -
user enters bill amount and receives a tip amount based on tip percentage

problems:
No option does not determine a new tip amount after re-rating the server. -  CONQUERED!
'''


''' Function payment
#The main function
#Check to see if the tip has been calculated using var tipcalculated
#asks for the bill amount
#asks for a rating, later used to determine the tippercent
#runs the tip function using the entered rating
#the function returns a tippercent
#as long as tipcalculated is False
#Asks for confirmation that the tip is okay.
#If yes, runs the calculator function using the entered values and produces the tip + total bill
#Returns tipcalculated as True, ending the application.
#If no, user will be asked to re-rate their server
#This will continue until the user is satisfied with the tip and accepts, enters Yes
'''


def payment(tipcalculated, splitnumber):
    if tipcalculated is False:
        check = int(input("What is your overall bill? "))
        rating = input("How would you rate your server 1 to 5? ")

        billamount = check / splitnumber

        tip(rating)
        tippercent = tip(rating)

        while tipcalculated is False:
            tipOK = str(input("You will tip " + str(int(tippercent * 100)) + "%. Is that okay? "))
            if tipOK == str("yes") or tipOK == str("y"):
                calculator(billamount, tippercent)
                tipcalculated = True
            if tipOK == str("no") or tipOK == str("n"):
                rating = input("How would you rate your server 1 to 5? ")
                tip(rating)
                tippercent = tip(rating)
                tipcalculated = False

''' Function calculator
#calculator figures out the tip amount
#and the informing how much the tip is
#and what the overall total is.
'''


def calculator(billamount, tippercent):

    tipamount = float(billamount) * float(tippercent)
    
    total = float(billamount) + float(tipamount)
    print(
        "{0}{1}".format("Please add ${0}".format(round(tipamount), 4), " for a total of ${0}".format(round(total), 2)))

    tipcalculated = True
    return tipcalculated

''' Function tip
#This is rating. Rating is translated into a
#tippercent that is used to calculate the
#over all tip amount.
'''


def tip(rating):
    tippercent = float(0)

    if rating == "1":
        tippercent = round(float(10.00), 2) * float(0.01)
    if rating == "2":
        tippercent = round(float(13.00), 2) * float(0.01)
    if rating == "3":
        tippercent = round(float(15.00), 2) * float(0.01)
    if rating == "4":
        tippercent = round(float(16.00), 2) * float(0.01)
    if rating == "5":
        tippercent = round(float(19.00), 2) * float(0.01)
    return tippercent


'''
#Creates var tipcalculated and sets to False
#Whenever tipcalculated is False
#Run payment function, checking for tipcalculated to be False
#Checks for tipcalculated to be True
'''


tipcalculated = False
split = input("Are you splitting the bill? ")
if split == "yes" or split == "y":
    splitnumber = int(input("How many checks? "))
    if tipcalculated is False:
        payment(tipcalculated, splitnumber)
        
if split == "no" or split == "no":
    splitnumber = 1
    if tipcalculated is False:
        payment(tipcalculated, splitnumber)

'''
if tipcalculated is False:
    payment(tipcalculated)
    print(tipcalculated)
'''










