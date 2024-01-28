from service import service_casino
from service import service_admin
from service import service_player
import random
    
def main():
    # load all data
    casino = service_casino.get_data()
    players = service_player.get_data()
    admins = service_admin.get_data()

    #try login
    print()
    logged_in = False
    while logged_in == False:
        logged_in = service_casino.login(admins)

    # static box instance and infinite loop
    bingo_box = tuple(range(1, 49))
    infinite_loop = True
    round = 1
    while(infinite_loop):
        # ask if there are new players here for register
        print()
        new_players = True
        while new_players == True:
            new_players = service_admin.ask_for_register(players)

        # write tickets
        print()
        write_tickets = True
        new_tickets = []
        while write_tickets == True:
            write_tickets  = service_player.write_ticket(players, new_tickets)

        print(f"--- CASINO: ${casino.name.upper()} - GAME STARTING -(Round: {round}--")
        print(f"--------------- GET ALL 6 WIN 500% -----------------\n")
        selected_numbers = random.sample(bingo_box, 6)
        selected_numbers.sort()
        print("Selected Numbers:")
        index = 1
        for number in selected_numbers:
            print(f"({index}) : {number}")
            index+= 1

        if len(new_tickets) > 0:
            for ticket in new_tickets:
                numbers_list = [int(num) for num in ticket.numbers.split(',')]
                numbers_list.sort()
                print("Ticket: ", numbers_list)
                if numbers_list == selected_numbers:
                    print("WE HAVE A WINNER: ", ticket.username)
                    print("PRIZE WON: ", float(ticket.bet) * 500)
                    break
            print("\nWe have no winner this round,")
        else:
            print(f"\nThere were no tickets this round.")

        round += 1
main()