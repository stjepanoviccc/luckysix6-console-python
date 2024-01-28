class Casino:

    def __init__(self, name, money):
        self._name = name
        self._money = money

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, new_money, case):
        if new_money < 0:
            print("You must enter valid amount of money to add/reduce")
            return
        if case == "ADD":
            self._money += new_money
        else:
            self._money -= new_money