pwd = input("What is the master password?")

def view():
    pass

view()

def add():
    name = input("Account Name:  ")
    pwd = input("Password:  ") 

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd )

while True:
    mode = input("Would you like to add a new password or view existing passwords? 'add' or 'view' or 'q' to quit  ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    if mode == "view":
        view()
    else:
        print("invalid mode")
        continue


