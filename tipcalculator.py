#tip calculator
#welcome to tip calculator
print("Welocome to the tip calculator:")
bill = float(input("What is the total bill ?\n"))
#decide the tip to be given
tip = int(input("what percentage tip would you like to give? 5, 10, 15\n"))
#distributed amongst how many people
people = int(input("How many people do you want to split the bill with?\n"))

bill_with_tip = tip / 100 * bill + bill
print("The total bill is:")
print(bill_with_tip)
print("and")

bill_each_Person_has_to_pay = bill_with_tip / people

print("Every person has to pay Rs:")
print(bill_each_person_has_to_pay)
