
import functions as f 


f.create_account()

id = f.log_in()
print(id)

f.make_deposit(id)

print("Your balance is: $" + str(f.check_balance(id)))

f.make_withdrawal(id)
choice = "password"
f.update_acc(id,choice)



 




 


 


