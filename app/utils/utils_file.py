import os
from model.admin import Admin
from model.player import Player
from model.casino import Casino

def read_all_admins(file_path):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'admin.txt')
    credentials = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password = line.strip().split('|')
            credentials.append(Admin(username, password))
    return credentials

def read_all_players(file_path):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'player.txt')
    credentials = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password, money = line.strip().split('|')
            credentials.append(Player(username, password, money))
    return credentials

def read_casino(file_path):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'casino.txt')
    with open(file_path, 'r') as file:
        for line in file:
            name, money = line.strip().split('|')
            return Casino(name, money)
        
def write_new_player(username, password, money):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'player.txt')
    with open(file_path, 'a') as file:
        file.write(f"{username}|{password}|{money}\n")

def overwrite_existing_player(username, money):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'player.txt')
    with open(file_path, 'r') as file:
        lines = [line.strip().split('|') for line in file]
    updated_lines = [
        f"{line[0]}|{line[1]}|{money}" if line[0] == username else "|".join(line)
        for line in lines
    ]
    with open(file_path, 'w') as file:
        file.write('\n'.join(updated_lines))

def write_new_ticket(username, bet, numbers):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'ticket.txt')
    with open(file_path, 'a') as file:
        file.write(f"{username}|{bet}|{numbers}")