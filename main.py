master_pwd = input("Please enter the master password: ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, passw = data.split('|')
            print("Username: ", username, "| Password: ", passw)

def add():
    acc_name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(acc_name + '|' + pwd + '\n')

while True:
    mode = input("Would you like to add new password or view your passwords?(type view, add or q to quit): ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mdoe")
        continue

#test