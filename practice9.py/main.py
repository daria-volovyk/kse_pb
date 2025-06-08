import data
import hashlib
user_status=False
current_user=None
def registration(users):
    login=input("Please enter your login")
    password=input("Please enter your password")
    password_hash=hashlib.sha256("{}".format(password).encode()).hexdigest()
    #print(password_hash)
    if login in users:
        print("username is already taken")
    else:
        users.update({login: password})
    return users

def login(users):
    name=input("Enter name")
    password=input("Please enter your password")
    password_hash=hashlib.sha256("{}".format(password).encode()).hexdigest()
    #print(password_hash)
    if name not in users:
        print("user is not registrated")
    else:
        if password_hash == users[name]:
            print("you are logged in")
            return True
    
def logout():
    return False

def send_email(users, emails):
    sender=
    recipient=input("enter recipient")
    mail=input("enter some text")
    if recipient not in users:
        print("not found")
    else:
        data.emails.append({"sender": sender, "recipient":recipient, "email":mail})

while True:
    try:
        user_choice=int(input("Enter your choice "))
    except Exception as e:
        print(e)
        user_choice=None
    if user_choice==0:
        break
    elif user_choice==1:
        if user_status is False:
            registration(data.users)
        else:
            print("you are logged in")
    elif user_choice==2:
        if user_status is False:
            user_status=login(data.users)

        else:
            print("you are logged in")
    elif user_choice==3:
        usser=input("Введіть своє ім'я")
        if user_status is True and usser=:
            send_email(data.users, data.emails)
        else:
            print("you are logged out")
    elif user_choice==4:
        if user_status is True:
            user_status = logout()
        else:
            print("You are not logged in")
        print("log out")
    elif user_choice==5:
        print(data.users)
        