from security.authentication.sign_in.sign_in import SignIn
from security.authentication.sign_up.sign_up import SignUp

if __name__ == '__main__':
    user = None
    while True:
        print("Choose an option:\n"
              "1 - Sign up\n"
              "2 - Sign in\n"
              "3 - Log out\n")
        option = int(input("Option: "))
        switcher = {
            1: SignUp.signup,
            2: SignIn.signin,
            3: SignIn.logout
        }
        option_func = switcher.get(option, "Invalid option")
        user = option_func()
        if user is not None:
            print(user.first_name, user.last_name)
