
def diagnose():
    print("Welcome to the Medical Diagnosis Expert System")


    fever = input("Do you have a fever? (yes/no): ").lower()
    cough = input("Do you have a cough? (yes/no): ").lower()
    rash = input("Do you have a rash? (yes/no): ").lower()


    if fever == 'yes' and cough == 'yes':
        return "Possible diagnosis: Influenza"
    elif fever == 'yes' and rash == 'yes':
        return "Possible diagnosis: Measles or Chickenpox"
    elif cough == 'yes' and rash == 'no':
        return "Possible diagnosis: Cold"
    else:
        return "Diagnosis uncertain. Please consult a doctor."


if __name__ == "__main__":
    result = diagnose()
    print(result)