from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Please enter the master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username, passw = data.split('|')
            print("Username: ", username, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    acc_name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(acc_name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

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