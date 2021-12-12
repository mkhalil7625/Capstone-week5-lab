"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3

def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')

def create_table():
    with sqlite3.connect('chainsaw_db.sqlite') as conn:# connect or create new dc
        conn.execute('CREATE TABLE if not exists record_holders (name text unique, country text, no_of_catches int)')
    conn.close()
create_table()
def insert_record_holder_data():
    with sqlite3.connect('chainsaw_db.sqlite') as conn:
        conn.execute('INSERT INTO record_holders VALUES ("Janne Mustonen","Finland",98)')
        conn.execute('INSERT INTO record_holders VALUES ("Ian Stewart","Canada",94)')
        conn.execute('INSERT INTO record_holders VALUES ("Aaron Gregg","Canada",88)')
        conn.execute('INSERT INTO record_holders VALUES ("Chad Taylor","USA",78)')
    conn.close()
insert_record_holder_data()
def display_all_records():
    conn = sqlite3.connect('chainsaw_db.sqlite')
    result = conn.execute('SELECT * FROM record_holders')
    print('All record holders: ')
    for row in result:
        print(row)
    conn.close()


def add_new_record():
    try:
        new_name = input("Enter player's name: ")
        new_country = input('Enter Country: ')
        new_catches = int(input('Enter number of catches: '))
            # do not use format strings with sql queries
        with sqlite3.connect('chainsaw_db.sqlite') as conn:
            conn.execute(f'INSERT INTO record_holders VALUES(?,?,?)',(new_name,new_country,new_catches))
        conn.close()
    except Exception as e:
        print("error inserting",e)


def edit_existing_record():
    try:
        updated_record=input("Enter the record holder's name that you would like to update: ")
        updated_no_of_catches=int(input("enter the new number of catches: "))
        with sqlite3.connect('chainsaw_db.sqlite') as conn:
            conn.execute('UPDATE record_holders SET no_of_catches = ? WHERE name = ?',(updated_no_of_catches,updated_record))
        conn.close()
    # print('todo edit existing record. What if user wants to edit record that does not exist?') 
    except Exception as e:
        print("error updating",e)

def delete_record():
    try:
        deleted_record=input("Enter the record holder's name that you would like to delete: ")
        with sqlite3.connect('chainsaw_db.sqlite') as conn:
            conn.execute('DELETE FROM record_holders WHERE name = ?',(deleted_record,))
        conn.close()
    except Exception as e:
        print("error deleting",e)
    # print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()