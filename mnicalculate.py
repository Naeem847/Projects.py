def get_input():
   flat_rent=int(input("enter your flat rent:\n"))
   total_food=int(input("enter your total food expense in a month:\n"))
   electricity_spent=int(input("enter total electricity unit consumed(KWH):\n"))
   charge_perunit=int(input("enter total charge per unit(KWH):\n"))
   total_person=int(input("enter total person living in room:\n"))
   total_bill=electricity_spent*charge_perunit
   print("total electricity bill in this month",total_bill)
   return flat_rent,total_food,total_person,electricity_spent,charge_perunit,total_bill

def show_total(flat_rent,total_food,total_bill,total_person):
  output=(flat_rent+total_food+total_bill)/total_person
  print("total expenses perperson:",output)
 
def show_rent(flat_rent):
  print("total rent_flat",flat_rent)
def show_food(total_food):
  print("total food expenses in this month:\n",total_food) 
def show_total_person(total_person):
  print("total person leave in this month:\n",total_person)
def show_bill(total_bill):
  print("total electricity bill per unit in this month:\n",total_bill)  
flat_rent, total_food, total_person, electricity_spent, charge_perunit, total_bill = get_input()
def main():
 while True:
      print("\n====MENU====")
      print("1.show flat rent")
      print("2.show food expwnses")
      print("3. total electricity bill in this month")
      print("4.show total per person expense")
      print("5.exit")
      choice=int(input("enter your choice:\n"))
      # flat_rent, total_food, total_person, electricity_spent, charge_perunit, total_bill = get_input()
      if choice==1:
       show_rent(flat_rent)
   
      elif choice==2:
       show_food(total_food)
      elif choice==3:
       show_bill(total_bill)
      elif choice==4:
       show_total(flat_rent,total_food,total_bill,total_person)
      elif choice==5:
       print("good bye exit the program")
       break
      else:
       print("invalid choice....")
main()
  