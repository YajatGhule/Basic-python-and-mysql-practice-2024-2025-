import os
import pickle
import csv
# 1. Text Files


def print_text_file(filename="students.txt"):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())


def insert_text_record(record, filename="students.txt"):
    with open(filename, 'a') as file:
        file.write(record + '\n')
    print(f"Record '{record}' inserted successfully.\n")


def search_text_record(query, filename="students.txt"):
    found_records = []
    with open(filename, 'r') as file:
        for line in file:
            if query in line:
                found_records.append(line.strip())
   
    if found_records:
        for record in found_records:
            print(record)
    else:
        print("No matching records found.")
def delete_word_from_text_file(word_to_delete, filename="students.txt"):
    word_found_in_file = False
    temp_filename = "temp.txt"
    with open(filename, 'r') as original_file, open(temp_filename, 'w') as temp_file:
        for line in original_file:
            words = line.split()
            new_words = []


            for word in words:
                if word == word_to_delete:
                    word_found_in_file = True
                else:
                    new_words.append(word)
           
            modified_line = " ".join(new_words) + "\n"
            temp_file.write(modified_line)
    os.remove(filename)
    os.rename(temp_filename, filename)
    if word_found_in_file:
        print(f"Word '{word_to_delete}' deleted successfully from the file.\n")
    else:
        print(f"Word '{word_to_delete}' not found in the file.\n")


# 2. Binary Files


def print_binary_file(filename="products.dat"):
    with open(filename, 'rb') as file:
        while True:
            try:
                data = pickle.load(file)
                print(data)
            except EOFError:
                break


def insert_binary_record(record, filename="products.dat"):
    with open(filename, 'ab') as file:
        pickle.dump(record, file)
    print(f"Record '{record}' inserted successfully.\n")


def search_binary_record(key, value, filename="products.dat"):
    found_records = []
    with open(filename, 'rb') as file:
        while True:
            try:
                record = pickle.load(file)
                if record.get(key) == value:
                    found_records.append(record)
            except EOFError:
                break
   
    if found_records:
        for record in found_records:
            print(record)
    else:
        print("No matching records found.")


def update_binary_record(record_id, new_record_data, filename="products.dat"):
    record_found = False
    temp_filename = "temp.dat"
    with open(filename, 'rb') as original_file, open(temp_filename, 'wb') as temp_file:
        while True:
            try:
                record = pickle.load(original_file)
                if record.get('id') == record_id:
                    pickle.dump(new_record_data, temp_file)
                    record_found = True
                else:
                    pickle.dump(record, temp_file)
            except EOFError:
                break
   
    os.remove(filename)
    os.rename(temp_filename, filename)


    if record_found:
        print(f"Record with ID '{record_id}' updated successfully.\n")
    else:
        print(f"Record with ID '{record_id}' not found.\n")


def delete_binary_record(record_id_to_delete, filename="products.dat"):
    record_found = False
    temp_filename = "temp.dat"
    with open(filename, 'rb') as original_file, open(temp_filename, 'wb') as temp_file:
        while True:
            try:
                record = pickle.load(original_file)
                if record.get('id') != record_id_to_delete:
                    pickle.dump(record, temp_file)
                else:
                    record_found = True
            except EOFError:
                break
   
    os.remove(filename)
    os.rename(temp_filename, filename)


    if record_found:
        print(f"Record with ID '{record_id_to_delete}' deleted successfully.\n")
    else:
        print(f"Record with ID '{record_id_to_delete}' not found.\n")


# 3. CSV Files


def print_csv_file(filename="employees.csv"):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def insert_csv_record(record_list, filename="employees.csv"):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(record_list)
    print(f"Record '{record_list}' inserted successfully.\n")


def search_csv_record(column_index, query, filename="employees.csv"):
    found_rows = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > column_index and row[column_index] == query:
                found_rows.append(row)


    if found_rows:
        for row in found_rows:
            print(row)
    else:
        print("No matching records found.")


def update_csv_record(record_id_to_update, new_row_data, filename="employees.csv"):
    record_found = False
    temp_filename = "temp.csv"
    with open(filename, 'r', newline='') as original_file, open(temp_filename, 'w', newline='') as temp_file:
        reader = csv.reader(original_file)
        writer = csv.writer(temp_file)
        for row in reader:
            if len(row) > 0 and row[0] == record_id_to_update:
                writer.writerow(new_row_data)
                record_found = True
            else:
                writer.writerow(row)
   
    os.remove(filename)
    os.rename(temp_filename, filename)


    if record_found:
        print(f"Record with ID '{record_id_to_update}' updated successfully.\n")
    else:
        print(f"Record with ID '{record_id_to_update}' not found.\n")


def delete_csv_record(record_id_to_delete, filename="employees.csv"):
    record_found = False
    temp_filename = "temp.csv"
    with open(filename, 'r', newline='') as original_file, open(temp_filename, 'w', newline='') as temp_file:
        reader = csv.reader(original_file)
        writer = csv.writer(temp_file)
        for row in reader:
            if len(row) > 0 and row[0] != record_id_to_delete:
                writer.writerow(row)
            else:
                record_found = True
   
    os.remove(filename)
    os.rename(temp_filename, filename)


    if record_found:
        print(f"Record with ID '{record_id_to_delete}' deleted successfully.\n")
    else:
        print(f"Record with ID '{record_id_to_delete}' not found.\n")      
#stacks
def push(stack,item):
    stack.append(item)
    top=len(stack)-1
def pop(stack):
    if stack == []:
        return 'undeflow'
    else:
        num=stack.pop()
        top=len(stack)-1
        return num
def peek(stack):
    if stack == []:
        return 'undeflow'
    else:
        top=len(stack)-1
        num=stack[top]
        return num
def display(stack):
    if stack == []:
        return 'undeflow'
    else:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
def PrintVote():
    F=open("Elections.txt")
    Lines=F.readlines()
    for Line in Lines:
        L=Line.split()
        if "vote" in L:
            print(Line)
    F.close()
