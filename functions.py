import mysql.connector

connection = mysql.connector.connect(user = "root", database = "esquivel_bank", password = "Sebas3107*")
cursor = connection.cursor()

def create_account():
    #Prompts user to enter account details and then adds data to the database
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birth_date = input("Enter your birthdate(month/day/year): ")
    address = input("Enter your current address: ")
    email = input("Enter your email: ")
    password = input("Enter your account password: ")
    balance = 0 

    addData = ("INSERT INTO user(firstname, lastname, birthdate, address, email, password, balance) VALUES( %s, %s, %s, %s,%s,%s,%s)")
    values = (first_name, last_name, birth_date, address, email, password, balance)

    cursor.execute(addData, values)
    connection.commit()

    print("Your account has been created.")

def log_in():
#This function prompts user to input an email in order to find a password from that email with a query
# Then we validate the password with a while loop
    e = input("Enter your email: ")
    #turns email from user into a list so we can find it through a query
    email = [e]

    query = ("SELECT password FROM user WHERE email = %s")
    
    password = input("Enter your password: ")

    cursor.execute(query , email)
    check = cursor.fetchone()
    #Until password isn't equal to the password in the query, you cannot go on.
    

    while password != check[0]:
        password = input("Wrong password, try again: ")
    
    print("You have logged in successfully!")
# Getting id will help identify the account in all the other functions:
    get_id = ("SELECT id FROM user WHERE email = %s")
    cursor.execute(get_id, email)
    id = cursor.fetchone()

    return id

def check_balance(id):
    query = ("SELECT balance FROM user WHERE id = %s")

    cursor.execute(query, id)
    balance = cursor.fetchone()

# Since cursor.fetchone() returns an iterable, we have to put index 0 next to it for the first value
    return balance[0]


def make_deposit(id):
#adds a specified amount to balance
    balance = int(input("How much money would you like to deposit?: $"))
    query = ("UPDATE user SET balance = balance + %s WHERE id = %s")
    value = (balance , id[0])

    cursor.execute(query, value)
    connection.commit()

def make_withdrawal(id):
#removes a specified amount from balance, unless the difference is less than 0
    balance = check_balance(id)
    amount = int(input("How much money would you like to withdraw?: $"))
    if (balance - amount) >= 0:
        query = ("UPDATE user SET balance = balance - %s WHERE id = %s")
        value = (amount , id[0])

        cursor.execute(query, value)
        connection.commit()
    else:
        print("Insufficient funds, we cannot make withdrawal. Your current balance is " + str(balance))

def delete_acc(id):
    #Deletes the user's account using the id
    query = ("DELETE FROM user WHERE id = %s")
    
    cursor.execute(query,id)

def update_acc(id, choice):
#This uses a choice parameter to create a query based on the detail they choose to modify
    if choice == "email":
        change = input("Enter new email: ")
        query = ("UPDATE user SET email = %s WHERE id = %s")
        values = (change, id[0])
        cursor.execute(query, values)
        connection.commit()
    elif choice == "password":
        change = input("Enter new password: ")
        query = ("UPDATE user SET password = %s WHERE id = %s")
        values = (change, id[0])
        cursor.execute(query, values)
        connection.commit()
    elif choice == "first name":
        change = input("Enter new name: ")
        query = ("UPDATE user SET firstname = %s WHERE id = %s")
        values = (change, id[0])
        cursor.execute(query, values)
        connection.commit()
    elif choice == "last name":
        change = input("Enter new last name: ")
        query = ("UPDATE user SET lastname = %s WHERE id = %s")
        values = (change, id[0])
        cursor.execute(query, values)
        connection.commit()
    elif choice == "address":
        change = input("Enter new address: ")
        query = ("UPDATE user SET address = %s WHERE id = %s")
        values = (change, id[0])
        cursor.execute(query, values)
        connection.commit()
    else:
        print("Invalid choice")