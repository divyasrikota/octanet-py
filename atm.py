class User:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

class ATM:
    def __init__(self):
        self.users = {} 
    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return True
        return False

    def withdraw(self, user_id, amount):
        if user_id in self.users:
            self.users[user_id].balance -= amount

    def deposit(self, user_id, amount):
        if user_id in self.users:
            self.users[user_id].balance += amount

    def transfer(self, sender_id, receiver_id, amount):
        if sender_id in self.users and receiver_id in self.users:
            self.users[sender_id].balance -= amount
            self.users[receiver_id].balance += amount

atm = ATM()
atm.users['divya'] = User('divya', '1234', 1000)

if atm.authenticate_user('divya', '1234'):
    atm.withdraw('divya',500)
    atm.deposit('divya',100)
    atm.transfer('divya', 'sri',200)
    print(f"balance after transactions: {atm.users['divya'].balance}")
else:
    print("Invalid credentials")
