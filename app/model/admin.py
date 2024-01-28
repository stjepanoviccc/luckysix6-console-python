from model.user import User

class Admin(User):
    
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if len(new_username) > 2:
            self._username = new_username
        else:
            print("Username must be longer than 2 letters!")

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, new_password):
        if len(new_password) > 2:
            self._password = new_password
        else:
            print("Password must be longer than 2 letters!")