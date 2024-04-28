
import functions as f 
from tkinter import *
import time


#f.create_account()
#id = f.log_in(email, password)
#print(id)
#f.make_deposit(id)
#print("Your balance is: $" + str(f.check_balance(id)))
#amount = int(input("How much money would you like to withdraw?: $"))
#f.make_withdrawal(id,amount)
#choice = "password"
#f.update_acc(id,choice)

root = Tk()
root.geometry("200x200")
root.columnconfigure((0,1,2,3,4), weight=50)
root.rowconfigure(0 , weight = 1)
root.rowconfigure((1,2,3,4), weight = 400)

title_frame = Frame(background="Light Gray", padx = 5, pady = 5, borderwidth = 2)
title_frame.grid(row = 0, column=0,columnspan= 5, sticky="nsew")

root.title("Esquivel Bank") 
Title_label = Label(root, text = "ESQUIVEL BANK",  font= ("Arial",20,"bold"), background= "Light Gray")
Title_label.place(x = 550 ,y = 10)
welcome_Label = Label(root, text= " Welcome to Esquivel Bank!")
welcome_Label.grid(row = 1, column=0, sticky="nw")
#Login entry spaces
email = Entry(root, width=50)
email.insert(0,"Enter email")
password = Entry(root, width=50)
password.insert(1,"Enter password")
email.place(x = 0, y = 120)
password.place(x = 0 , y = 160)

#email entry spaces
firstname = Entry(root, width = 50)
firstname.insert(3, "Enter First Name:")
firstname.place(x = 0 , y = 300)

lastname = Entry(root, width = 50)
lastname.insert(3, "Enter Last Name:")
lastname.place(x = 0 , y = 340)

birthdate = Entry(root, width = 50)
birthdate.insert(3, "Enter Birth Date(mm/dd/yyyy):")
birthdate.place(x = 0 , y = 380)

address = Entry(root, width = 50)
address.insert(3, "Enter Address:")
address.place(x = 0 , y = 420)

email_2 = Entry(root, width = 50)
email_2.insert(3, "Enter Email:")
email_2.place(x = 0 , y = 460)

password_2 = Entry(root, width = 50)
password_2.insert(3, "Enter Password:")
password_2.place(x = 0 , y = 500)




def login_entry():
    log = f.log_in(email.get(),password.get())
    if log == True:
        log_label = Label(root, text= "Logged in successfully!")
        log_label.place(x = 0, y = 220)
        e = [email.get()]
        global id
        id = f.get_id(e)
        #Options appear after this line
        check_balance_button.place(x = 400, y = 100)
        make_deposit_button.place(x = 400, y = 200 )
        deposit.place(x = 600, y = 230)
        make_withdrawal_button.place(x = 400, y = 300 )
        withdrawal.place(x = 600, y = 330)
        update_button.place(x = 400, y = 400)
        update.place(x = 600, y = 430)
        update2.place(x = 950, y = 430)
        delete_button.place(x = 400, y = 500 )

    elif log == False:
        log_label = Label(root, text= "Wrong email or password, try again")
        log_label.place(x = 0, y = 200)
    
def acc_entry():
    f.create_account(firstname.get(),lastname.get(),birthdate.get(),address.get(),email_2.get(),password_2.get())
    acc_label = Label(root, text= "Account created successfully! Now log in")
    acc_label.place(x = 0, y = 540)


    

    
login_button = Button(root, text ="Log into account", command= login_entry)
email_button = Button(root, text = "Create an account", command=acc_entry)





login_button.grid(row = 1, column = 0, sticky = "w")
email_button.place(x = 0, y = 260)


def check_balance_entry():
    balance = f.check_balance(id)
    balance_label = Label(root, text=("Your balance is: $" + str(balance)))
    balance_label.place(x = 600, y = 130)

def make_deposit_entry():
    f.make_deposit(id, int(deposit.get()))

def make_withdrawal_entry():
    failure_label = Label(root, text=("Insufficient funds, deposit more or withdraw less."))
    success_label = Label(root, text=("Successful withdrawal!"), width=40)
    w = f.make_withdrawal(id,int(withdrawal.get()))
    if not w:
        failure_label.place(x = 800, y = 330)
        
    else:
        success_label.place(x = 800, y = 330)
    
def update_entry():
    f.update_acc(id, update.get(),update2.get())
    update_label = Label(root, text=("Account has been successfully modified"))
    update_label.place(x = 950, y = 400) 

def delete_entry():
    f.delete_acc(id)
    delete_label = Label(root, text=("Your account has been deleted."))
    delete_label.place(x = 600, y = 530)

check_balance_button = Button(root, text="Check Balance", height=5, width= 20, command=check_balance_entry)


make_deposit_button = Button(root, text="Make deposit", height=5, width= 20, command=make_deposit_entry)

deposit = Entry(root, width = 20)
deposit.insert(3,"Deposit amount: ")


make_withdrawal_button = Button(root, text="Make withdrawal", height=5, width= 20, command=make_withdrawal_entry)

withdrawal = Entry(root, width = 20)
withdrawal.insert(3,"Withdrawal amount: ")


update_button = Button(root, text="Modify account details", height=5, width= 20, command=update_entry)

update = Entry(root, width = 45)
update.insert(3,"Enter account detail you would like to update: ")

update2 = Entry(root, width = 25)
update2.insert(3,"Enter desired change: ")


delete_button = Button(root, text="Delete Account", height=5, width= 20, command=delete_entry)

    
    



root.mainloop()
