from utils import utils_file
from model.casino import Casino

def get_data():
    return utils_file.read_casino("data/casino.txt")

def login(admins):
    print("\n-------------------- LOG IN SCREEN --------------------\n")
    print("Hello Admin.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for i in admins:
        if username == i.username and password == i.password:
            print("Logged in successful. Welcome", username)
            return True
    print("Login failed. Try again.")
    return False