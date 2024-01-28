from utils import utils_file
from model.player import Player
from model.ticket import Ticket

def get_data():
    return utils_file.read_all_players("data/player.txt")

def write_ticket(players, new_tickets):
    case = input("\nPlace bet? Type '0' to refuse: ")
    if case == '0':
        return False
    username = input("Type your username: ")
    password = input("Type your password: ")
    bet = input("Type money amount to place on bet: ")
    numbers = input("Type numbers from 1 to 48 separated by commas: ")
    for i in players:
        if i.username == username and i.password == password:
            existing_money = float(i.money)
            if float(bet) <= existing_money:
                existing_money -= float(bet)
                utils_file.overwrite_existing_player(username, existing_money)
                utils_file.write_new_ticket(username, bet, numbers)
                new_tickets.append(Ticket(username, bet, numbers))
                return True
            else:
                print("You don't have enough money\n")
                return True
    print("Wrong credentials. Try again\n")
    return True
    