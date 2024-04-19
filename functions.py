import mysql.connector

connection = mysql.connector.connect(user = "root", database = "esquivel_bank", password = "Sebas3107*")
cursor = connection.cursor()

def create_account():
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
    e = input("Enter your email: ")
    #turns email from user into tuple so we can find it through a query
    email = [e]

    query = ("SELECT password FROM user WHERE email = %s")
    
    password = input("Enter your password: ")

    cursor.execute(query , email)
    check = cursor.fetchone()
    #Until password isn't equal to the password in the query, you cannot go on.
    

    while password != check[0]:
        password = input("Wrong password, try again: ")
    
    print("You have logged in successfully!")

    return email

def check_balance(email):
    query = ("SELECT balance FROM user WHERE email = %s")

    cursor.execute(query, email)
    balance = cursor.fetchone()

    print("Your balance is: $" + str(balance[0]))

def make_deposit(email):
    balance = int(input("How much money would you like to deposit?: $"))
    query = ("UPDATE user SET balance = balance + %s WHERE email = %s")
    value = (balance , email[0])

    cursor.execute(query, value)
    connection.commit()

    





    





    
    
    
    
    

        













