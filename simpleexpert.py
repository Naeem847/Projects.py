print("=== BASIC DISEASE EXPERT SYSTEM ===")
fever = input("Do you have fever? ").lower()
cough = input("Do you have cough? ").lower()
headache = input("Do you have headache? ").lower()
if fever == "yes" and cough == "yes":
 print("Diagnosis: Flu")
elif cough == "yes" and headache == "yes":
 print("Diagnosis: Common Cold")
else:
 print("No disease matched.")