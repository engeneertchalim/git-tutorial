

def get_username():
    return input("Username: ")


def get_email():
    return input("Email address: ")



def get_password():
    return input("Password:")


username = get_username()

email = get_email()

password = get_password()


def registration(username, email, password):

    print("account created successful")

    print("saving user in database")


registration(username=username, email=email, password=password)