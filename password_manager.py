pwd = input("What is the master password?")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User: " + user + " Password: " + passwd)




def add():
    name = input("Account Name:  ")
    pwd = input("Password:  ") 

    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + pwd  + "\n")

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


