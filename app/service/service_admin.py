from utils import utils_file
from model.player import Player

def get_data():
    data = utils_file.read_all_admins("data/admin.txt")
    return data

def ask_for_register(players):
    case = input("Add new player? Type '0' to refuse: ")
    if case == '0':
        return False
    username = input("Type new player username: ")
    password = input("Type new plaer password: ")
    money = input("Type new player money ammount: ")
    utils_file.write_new_player(username,password, money)    
    players.append(Player(username, password, money))
    return True
