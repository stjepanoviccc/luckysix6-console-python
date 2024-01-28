from abc import ABC, abstractmethod

class User(ABC):

    @property
    @abstractmethod
    def username(self):
        pass

    @username.setter
    @abstractmethod
    def username(self, new_username):
        pass

    @property
    @abstractmethod
    def password(self):
        pass

    @password.setter
    @abstractmethod
    def password(self, new_password):
        pass