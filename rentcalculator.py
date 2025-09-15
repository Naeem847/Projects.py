def hello():

 flat_rent=int(input("enter your flat rent:\n"))
 total_food=int(input("enter your total food in a month:\n"))
 electricity_spent=int(input("enter total electricity unit consumed(KWH):\n"))
 charge_perunit=int(input("enter total charge per unit(KWH):\n"))
 total_person=int(input("enter total person living in room:\n"))
 total_bill=electricity_spent*charge_perunit
 
 output=flat_rent+total_food+electricity_spent+charge_perunit+total_bill/3
 print("total spent money in this month is:",output)
hello()