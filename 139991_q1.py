"""simplified patient management system for a hospital."""
"""This function is to add names of patients into the system"""           
def add_patient(patients, name, age, illness):
    patient = {
        'name': name,
        'age': age,
        'illness': illness
    }
    patients.append(patient)
    print(f"Patient {name} added.")

def display_patients(patients):
    if not patients:
        print("No patients found.")
    for patient in patients:
        print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(patients, name):
    for patient in patients:
        if patient['name'] == name:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print("Patient not found.")

def remove_patient(patients, name):
    for i, patient in enumerate(patients):
        if patient['name'] == name:
            del patients[i]
            print(f"Patient {name} removed.")
            return
    print("Patient not found.")

def main():
    patients = []  # Initialize an empty list to store patient records
    
    while True:
        print("\nMenu:")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            illness = input("Enter patient's illness: ")
            add_patient(patients, name, age, illness)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            name = input("Enter patient's name to search: ")
            search_patient(patients, name)
        elif choice == '4':
            name = input("Enter patient's name to remove: ")
            remove_patient(patients, name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Starting the Patient Management System...")
    main()
