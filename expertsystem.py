def medical_expert_system():
    print("===== MEDICAL EXPERT SYSTEM =====")
    fever = input("Do you have fever? (yes/no): ").lower()
    cough = input("Do you have cough? (yes/no): ").lower()
    headache = input("Do you have headache? (yes/no): ").lower()
    sore_throat = input("Do you have sore throat? (yes/no): ").lower()
    print("\nDiagnosis Result:")
    # Rule-based reasoning
    if fever == 'yes' and cough == 'yes' and headache == 'yes':
        print("You may have FLU.")
    elif fever == 'yes' and sore_throat == 'yes':
        print("You may have THROAT INFECTION.")
    elif cough == 'yes' and sore_throat == 'yes':
        print("You may have COMMON COLD.")
    else:
        print("No serious illness detected.")
    print("================================")
# Run the expert system
medical_expert_system()