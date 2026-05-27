import mysql.connector as s
#use s.connection for some computers its diffrent tldr(its your systems problem not mine
#check youe .env variables if your using vs code or vim , for idle just use normally 
#for EXPORT functions vs code is funny and wont do it properly 
#this is the main program it might need coorection later on and new features added 
sq= s.MySQLConnection(host='localhost',user='root',password='password',database='hospital')
c=sq.cursor()
print("Connection status:", sq.is_connected())
#gui nees confirmation from ramya mam if its fine to use ai 
def add_record(table):
    if table == 1:
        employee_id = input("Enter the employee ID you wish to add: ")
        name = input("Enter the name of the employee: ")
        city = input("Enter the city of the employee: ")
        salary = float(input('Enter the salary of the employee: '))
        shift = input("Enter the shift of the employee (day or night only): ")
        query = f'insert into Employee values("{employee_id}", "{name}", "{city}", {salary}, "{shift}")'
        print(query)
        c.execute(query)
        sq.commit()
        print("Employee record inserted successfully.")
        return True
    elif table == 2:
        doctor_id = int(input("Enter the doctor id (pk): "))
        name = input(f"Enter the name of doctor {doctor_id}: ")
        specialty = input(f"Enter specialty of doctor {doctor_id}: ")
        phno = int(input(f"Enter the phone number of doctor {doctor_id}: "))
        email = input(f"Enter the email of doctor {doctor_id}: ")
        address = input(f"Enter the address of doctor {doctor_id}: ")
        query = f'insert into doctor values({doctor_id}, "{name}", "{specialty}", {phno}, "{email}", "{address}")'
        print(query)
        c.execute(query)
        sq.commit()
        print("Doctor record inserted successfully.")
        return True
    elif table == 3:
        visitor_id = int(input("Enter the visitor id (pk): "))
        first_name = input("Enter the first name of the visitor: ")
        last_name = input("Enter the last name of the visitor: ")
        email = input("Enter the email of the visitor: ")
        phone_number = input("Enter the phone number of the visitor: ")
        time_of_arrival = input("Enter the time of arrival (e.g. 10:00): ")
        time_of_departure = input("Enter the time of departure (e.g. 18:00): ")
        query = f'insert into visitor values({visitor_id}, "{first_name}", "{last_name}", "{email}", "{phone_number}", "{time_of_arrival}", "{time_of_departure}")'
        print(query)
        c.execute(query)
        sq.commit()
        print("Visitor record inserted successfully.")
        return True
    elif table == 4:
        nurse_id = int(input("Enter the nurse id (pk): "))
        first_name = input("Enter the first name of the nurse: ")
        last_name = input("Enter the last name of the nurse: ")
        gender = input("Enter the gender of the nurse (m/f): ")
        employee_id = input("Enter the employee id for the nurse: ")
        contact_number = input("Enter the contact number of the nurse: ")
        email = input("Enter the email of the nurse: ")
        hire_date = input("Enter the hire date (yyyy-mm-dd): ")
        query = f'insert into nurses values({nurse_id}, "{first_name}", "{last_name}", "{gender}", "{employee_id}", "{contact_number}", "{email}", "{hire_date}")'
        print(query)
        c.execute(query)
        sq.commit()
        print("Nurse record inserted successfully.")
        return True
    elif table == 5:
        patient_id = int(input("Enter the patient id (pk): "))
        name = input("Enter the name of the patient: ")
        dob = input("Enter the date of birth (yyyy-mm-dd): ")
        gender = input("Enter the gender (m/f): ")
        blood_grp = input("Enter the blood group: ")
        illness = input("Enter the illness: ")
        doc_id = int(input("Enter the doctor id: "))
        doc_name = input("Enter the doctor name: ")
        address = input("Enter the address: ")
        contact_number = input("Enter the contact number: ")
        email = input("Enter the email: ")
        query = f'insert into patient values({patient_id}, "{name}", "{dob}", "{gender}", "{blood_grp}", "{illness}", {doc_id}, "{doc_name}", "{address}", "{contact_number}", "{email}")'
        print(query)
        c.execute(query)
        sq.commit()
        print("Patient record inserted successfully.")
        return True
    else:
        print("Invalid table selection.")
        return None
def update_table(table):
    if table == 1:
        employee_id = input("Enter the employee ID you wish to update: ")
        print("Which field do you want to update?")
        print("1. Name")
        print("2. City")
        print("3. Salary")
        print("4. Shift")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            new_name = input("Enter the new name: ")
            query = f'update Employee set name="{new_name}" where employee_id="{employee_id}"'
        elif choice == 2:
            new_city = input("Enter the new city: ")
            query = f'update Employee set city="{new_city}" where employee_id="{employee_id}"'
        elif choice == 3:
            new_salary = float(input("Enter the new salary: "))
            query = f'update Employee set salary={new_salary} where employee_id="{employee_id}"'
        elif choice == 4:
            new_shift = input("Enter the new shift (day or night only): ")
            query = f'update Employee set shift="{new_shift}" where employee_id="{employee_id}"'
        else:
            print("Invalid choice.")
            return None
        print(query)
        c.execute(query)
        sq.commit()
        print("Employee record updated successfully.")
        return True
    elif table == 2:
        doctor_id = int(input("Enter the doctor id (pk) you wish to update: "))
        print("Which field do you want to update?")
        print("1. Name")
        print("2. Specialty")
        print("3. Phone Number")
        print("4. Email")
        print("5. Address")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            new_name = input("Enter the new name: ")
            query = f'update doctor set name="{new_name}" where doctor_id={doctor_id}'
        elif choice == 2:
            new_specialty = input("Enter the new specialty: ")
            query = f'update doctor set specialty="{new_specialty}" where doctor_id={doctor_id}'
        elif choice == 3:
            new_phno = int(input("Enter the new phone number: "))
            query = f'update doctor set phno={new_phno} where doctor_id={doctor_id}'
        elif choice == 4:
            new_email = input("Enter the new email: ")
            query = f'update doctor set email="{new_email}" where doctor_id={doctor_id}'
        elif choice == 5:
            new_address = input("Enter the new address: ")
            query = f'update doctor set address="{new_address}" where doctor_id={doctor_id}'
        else:
            print("Invalid choice.")
            return None
        print(query)
        c.execute(query)
        sq.commit()
        print("Doctor record updated successfully.")
        return True
    elif table == 3:
        visitor_id = int(input("Enter the visitor id (pk) you wish to update: "))
        print("Which field do you want to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Email")
        print("4. Phone Number")
        print("5. Time of Arrival")
        print("6. Time of Departure")
        choice = int(input("Enter your choice (1-6): "))
        if choice == 1:
            new_first_name = input("Enter the new first name: ")
            query = f'update visitor set first_name="{new_first_name}" where visitor_id={visitor_id}'
        elif choice == 2:
            new_last_name = input("Enter the new last name: ")
            query = f'update visitor set last_name="{new_last_name}" where visitor_id={visitor_id}'
        elif choice == 3:
            new_email = input("Enter the new email: ")
            query = f'update visitor set email="{new_email}" where visitor_id={visitor_id}'
        elif choice == 4:
            new_phone_number = input("Enter the new phone number: ")
            query = f'update visitor set phone_number="{new_phone_number}" where visitor_id={visitor_id}'
        elif choice == 5:
            new_time_of_arrival = input("Enter the new time of arrival (e.g. 10:00): ")
            query = f'update visitor set time_of_arrival="{new_time_of_arrival}" where visitor_id={visitor_id}'
        elif choice == 6:
            new_time_of_departure = input("Enter the new time of departure (e.g. 18:00): ")
            query = f'update visitor set time_of_departure="{new_time_of_departure}" where visitor_id={visitor_id}'
        else:
            print("Invalid choice.")
            return None
        print(query)
        c.execute(query)
        sq.commit()
        print("Visitor record updated successfully.")
        return True
    elif table == 4:
        nurse_id = int(input("Enter the nurse id (pk) you wish to update: "))
        print("Which field do you want to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Gender")
        print("4. Employee ID")
        print("5. Contact Number")
        print("6. Email")
        print("7. Hire Date")
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            new_first_name = input("Enter the new first name: ")
            query = f'update nurses set first_name="{new_first_name}" where nurse_id={nurse_id}'
        elif choice == 2:
            new_last_name = input("Enter the new last name: ")
            query = f'update nurses set last_name="{new_last_name}" where nurse_id={nurse_id}'
        elif choice == 3:
            new_gender = input("Enter the new gender (m/f): ")
            query = f'update nurses set gender="{new_gender}" where nurse_id={nurse_id}'
        elif choice == 4:
            new_employee_id = input("Enter the new employee id: ")
            query = f'update nurses set employee_id="{new_employee_id}" where nurse_id={nurse_id}'
        elif choice == 5:
            new_contact_number = input("Enter the new contact number: ")
            query = f'update nurses set contact_number="{new_contact_number}" where nurse_id={nurse_id}'
        elif choice == 6:
            new_email = input("Enter the new email: ")
            query = f'update nurses set email="{new_email}" where nurse_id={nurse_id}'
        elif choice == 7:
            new_hire_date = input("Enter the new hire date (yyyy-mm-dd): ")
            query = f'update nurses set hire_date="{new_hire_date}" where nurse_id={nurse_id}'
        else:
            print("Invalid choice.")
            return None
        print(query)
        c.execute(query)
        sq.commit()
        print("Nurse record updated successfully.")
        return True
    elif table == 5:
        patient_id = int(input("Enter the patient id (pk) you wish to update: "))
        print("Which field do you want to update?")
        print("1. Name")
        print("2. DOB")
        print("3. Gender")
        print("4. Blood Group")
        print("5. Illness")
        print("6. Doctor ID")
        print("7. Doctor Name")
        print("8. Address")
        print("9. Contact Number")
        print("10. Email")
        choice = int(input("Enter your choice (1-10): "))
        if choice == 1:
            new_name = input("Enter the new name: ")
            query = f'update patient set name="{new_name}" where patient_id={patient_id}'
        elif choice == 2:
            new_dob = input("Enter the new date of birth (yyyy-mm-dd): ")
            query = f'update patient set dob="{new_dob}" where patient_id={patient_id}'
        elif choice == 3:
            new_gender = input("Enter the new gender (m/f): ")
            query = f'update patient set gender="{new_gender}" where patient_id={patient_id}'
        elif choice == 4:
            new_blood_grp = input("Enter the new blood group: ")
            query = f'update patient set blood_grp="{new_blood_grp}" where patient_id={patient_id}'
        elif choice == 5:
            new_illness = input("Enter the new illness: ")
            query = f'update patient set illness="{new_illness}" where patient_id={patient_id}'
        elif choice == 6:
            new_doc_id = int(input("Enter the new doctor id: "))
            query = f'update patient set doc_id={new_doc_id} where patient_id={patient_id}'
        elif choice == 7:
            new_doc_name = input("Enter the new doctor name: ")
            query = f'update patient set doc_name="{new_doc_name}" where patient_id={patient_id}'
        elif choice == 8:
            new_address = input("Enter the new address: ")
            query = f'update patient set address="{new_address}" where patient_id={patient_id}'
        elif choice == 9:
            new_contact_number = input("Enter the new contact number: ")
            query = f'update patient set contact_number="{new_contact_number}" where patient_id={patient_id}'
        elif choice == 10:
            new_email = input("Enter the new email: ")
            query = f'update patient set email="{new_email}" where patient_id={patient_id}'
        else:
            print("Invalid choice.")
            return None
        print(query)
        c.execute(query)
        sq.commit()
        print("Patient record updated successfully.")
        return True
    else:
        print("Invalid table selection.")
        return None
def delete_record(table):
    if table == 1:
        employee_id = input("Enter the employee ID you wish to delete: ")
        query = f'delete from Employee where employee_id="{employee_id}"'
        print(query)
        c.execute(query)
        sq.commit()
        print("Employee record deleted successfully.")
        return True
    elif table == 2:
        doctor_id = int(input("Enter the doctor id (pk) you wish to delete: "))
        query = f'delete from doctor where doctor_id={doctor_id}'
        print(query)
        c.execute(query)
        sq.commit()
        print("Doctor record deleted successfully.")
        return True
    elif table == 3:
        visitor_id = int(input("Enter the visitor id (pk) you wish to delete: "))
        query = f'delete from visitor where visitor_id={visitor_id}'
        print(query)
        c.execute(query)
        sq.commit()
        print("Visitor record deleted successfully.")
        return True
    elif table == 4:
        nurse_id = int(input("Enter the nurse id (pk) you wish to delete: "))
        query = f'delete from nurses where nurse_id={nurse_id}'
        print(query)
        c.execute(query)
        sq.commit()
        print("Nurse record deleted successfully.")
        return True
    elif table == 5:
        patient_id = int(input("Enter the patient id (pk) you wish to delete: "))
        query = f'delete from patient where patient_id={patient_id}'
        print(query)
        c.execute(query)
        sq.commit()
        print("Patient record deleted successfully.")
        return True
    else:
        print("Invalid table selection.")
        return None
def display_records(table):
    if table == 1:
        query = 'select * from Employee'
        c.execute(query)
        records = c.fetchall()
        print("Employee Records:")
        for row in records:
            print(row)
        return True
    elif table == 2:
        query = 'select * from doctor'
        c.execute(query)
        records = c.fetchall()
        print("Doctor Records:")
        for row in records:
            print(row)
        return True
    elif table == 3:
        query = 'select * from visitor'
        c.execute(query)
        records = c.fetchall()
        print("Visitor Records:")
        for row in records:
            print(row)
        return True
    elif table == 4:
        query = 'select * from nurses'
        c.execute(query)
        records = c.fetchall()
        print("Nurse Records:")
        for row in records:
            print(row)
    elif table == 5:
        query = 'select * from patient'
        c.execute(query)
        records = c.fetchall()
        print("Patient Records:")
        for row in records:
            print(row)
        return True
    else:
        print("Invalid table selection.")
        return None
def search_records(table):
    if table == 1:
        print("Search Employee by:")
        print("1. ID")
        print("2. Name")
        print("3. City")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            employee_id = input("Enter the employee ID: ")
            query = f'select * from Employee where employee_id="{employee_id}"'
        elif choice == 2:
            name = input("Enter the employee name: ")
            query = f'select * from Employee where name="{name}"'
        elif choice == 3:
            city = input("Enter the employee city: ")
            query = f'select * from Employee where city="{city}"'
        else:
            print("Invalid choice.")
            return None
        c.execute(query)
        records = c.fetchall()
        print("Search Results:")
        for row in records:
            print(f'ID: {row[0]}, Name: {row[1]}, City: {row[2]}, Salary: {row[3]}, Shift: {row[4]}')
        return True
    elif table == 2:
        print("Search Doctor by:")
        print("1. ID")
        print("2. Name")
        print("3. Specialty")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            doctor_id = int(input("Enter the doctor ID: "))
            query = f'select * from doctor where doctor_id={doctor_id}'
        elif choice == 2:
            name = input("Enter the doctor name: ")
            query = f'select * from doctor where name="{name}"'
        elif choice == 3:
            specialty = input("Enter the doctor specialty: ")
            query = f'select * from doctor where specialty="{specialty}"'
        else:
            print("Invalid choice.")
            return None
        c.execute(query)
        records = c.fetchall()
        print("Search Results:")
        for row in records:
            print(f'ID: {row[0]}, Name: {row[1]}, Specialty: {row[2]}, Phone Number: {row[3]}, Email: {row[4]}, Address: {row[5]}')
        return True
    elif table == 3:
        print("Search Visitor by:")
        print("1. ID")
        print("2. First Name")
        print("3. Last Name")
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            visitor_id = int(input("Enter the visitor ID: "))
            query = f'select * from visitor where visitor_id={visitor_id}'
        elif choice == 2:
            first_name = input("Enter the visitor first name: ")
            query = f'select * from visitor where first_name="{first_name}"'
        elif choice == 3:   
            last_name = input("Enter the visitor last name: ")
            query = f'select * from visitor where last_name="{last_name}"'
        else:
            print("Invalid choice.")
            return None
        c.execute(query)
        records = c.fetchall()
        print("Search Results:")
        for row in records:
            print(f'ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Email: {row[3]}, Phone Number: {row[4]}, Time of Arrival: {row[5]}, Time of Departure: {row[6]}')
        return True
    elif table == 4:
        print("Search Nurse by:")
        print("1. ID")
        print("2. First Name")
        print("3. Last Name")
        print("4. Email")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            nurse_id = int(input("Enter the nurse ID: "))
            query = f'select * from nurses where nurse_id={nurse_id}'
        elif choice == 2:
            first_name = input("Enter the nurse first name: ")
            query = f'select * from nurses where first_name="{first_name}"'
        elif choice == 3:
            last_name = input("Enter the nurse last name: ")
            query = f'select * from nurses where last_name="{last_name}"'
        elif choice == 4:
            email = input("Enter the nurse email: ")
            query = f'select * from nurses where email="{email}"'
        else:
            print("Invalid choice.")
            return None
        c.execute(query)
        records = c.fetchall()
        print("Search Results:")
        for row in records:
            print(f'ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Gender: {row[3]}, Employee ID: {row[4]}, Contact Number: {row[5]}, Email: {row[6]}, Hire Date: {row[7]}')
        return True
    elif table == 5:
        print("Search Patient by:")
        print("1. ID")
        print("2. Name")
        print("3. Illness")
        print("4. Doctor Name")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            patient_id = int(input("Enter the patient ID: "))
            query = f'select * from patient where patient_id={patient_id}'
        elif choice == 2:
            name = input("Enter the patient name: ")
            query = f'select * from patient where name="{name}"'
        elif choice == 3:
            illness = input("Enter the illness: ")
            query = f'select * from patient where illness="{illness}"'
        elif choice == 4:
            doc_name = input("Enter the doctor name: ")
            query = f'select * from patient where doc_name="{doc_name}"'
        else:
            print("Invalid choice.")
            return None
        c.execute(query)
        records = c.fetchall()
        print("Search Results:")
        for row in records:
            print(f'ID: {row[0]}, Name: {row[1]}, DOB: {row[2]}, Gender: {row[3]}, Blood Group: {row[4]}, Illness: {row[5]}, Doctor ID: {row[6]}, Doctor Name: {row[7]}, Address: {row[8]}, Contact Number: {row[9]}, Email: {row[10]}')
        return True
    else:
        print("Invalid table selection.")
        return None
def main():
    while True:
        print("\nHospital Management System")
        print("1. Add Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. Display Records")
        print("5. Search Records")
        print("6. Exit")
        choice = int(input("Enter your choice (1-6): "))
        if choice == 7:
            print("Exiting the program.")
            break
        print("Select Table:")
        print("1. Employee")
        print("2. Doctor")
        print("3. Visitor")
        print("4. Nurse")
        print("5. Patient")
        table = int(input("Enter your choice (1-5): "))
        if choice == 1:
            add_record(table)
        elif choice == 2:
            update_table(table)
        elif choice == 3:
            delete_record(table)
        elif choice == 4:
            display_records(table)
        elif choice == 5:
            search_records(table)
        elif choice ==6:
            csv_export(table)
            
        else:
            print("Invalid choice, please try again.")
def csv_export(table):
    import csv
    if table == 1:
        query = 'select * from employee'
        c.execute(query)
        records = c.fetchall()
        with open('employee_records.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'City', 'Salary', 'Shift'])
            for row in records:
                writer.writerow(row)
        print("Employee records exported to employee_records.csv")
    elif table == 2:
        query = 'select * from doctor'
        c.execute(query)
        records = c.fetchall()
        with open('doctor_records.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Specialty', 'Phone Number', 'Email', 'Address'])
            for row in records:
                writer.writerow(row)
        print("Doctor records exported to doctor_records.csv")
    elif table == 3:
        query = 'select * from visitor'
        c.execute(query)
        records = c.fetchall()
        with open('visitor_records.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Time of Arrival', 'Time of Departure'])
            for row in records:
                writer.writerow(row)
        print("Visitor records exported to visitor_records.csv")
    elif table == 4:
        query = 'select * from nurses'
        c.execute(query)
        records = c.fetchall()
        with open('nurse_records.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'First Name', 'Last Name', 'Gender', 'Employee ID', 'Contact Number', 'Email', 'Hire Date'])
            for row in records:
                writer.writerow(row)
        print("Nurse records exported to nurse_records.csv")
    elif table == 5:
        query = 'select * from patient'
        c.execute(query)
        records = c.fetchall()
        with open('patient_records.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'DOB', 'Gender', 'Blood Group', 'Illness', 'Doctor ID', 'Doctor Name', 'Address', 'Contact Number', 'Email'])
            for row in records:
                writer.writerow(row)
        print("Patient records exported to patient_records.csv")
    else:
        print("Invalid table selection.")
        return None
if __name__ == "__main__":
    main()
    # Uncomment the following lines u srg person    
    # # csv_export(1)
    # csv_export(2)
# csv_export(3)  
    c.close()
    sq.close()
    print("Connection closed.")
