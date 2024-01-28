class Ticket():
    
    def __init__(self, username, bet, numbers):
        self._username = username
        self._bet = bet
        self._numbers = numbers
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def bet(self):
        return self._bet
    
    @bet.setter
    def bet(self, new_bet):
        self._bet = new_bet

    @property
    def numbers(self):
        return self._numbers
    
    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers