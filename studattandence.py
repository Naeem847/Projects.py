
while True:
   stud_data={
    "student1":{"name":"naeem","mis_id":25599},
    "student2":{"name":"ali","mis_id":24466},
    "student3":{"name":"hassan","mis_id":23377},
   }

   name=(input("enter your name or you exit project\n"))
   if name.lower()=="exit":
      print("exiting the attandence goodbye")
      break
  
   mis_id_input=(input("enter your mis_id or you exit project:\n"))
   if mis_id_input.lower()=="exit":
    print("exiting the attandence goodbye")
    break
 
   mis_id = int(mis_id_input)
   for student in stud_data.values():
      if student["name"]==name and student["mis_id"]==mis_id:
        print("present")
        break
   else:
    print("absent")
 