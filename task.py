import logging

class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def add_client(self, name, balance=0):
        self.clients[name] = balance

    def deposit(self, name, amount):
        if name in self.clients:
            self.clients[name] += amount
        else:
            logging.warning("Clients not found.")

    def withdraw(self, name, amount):
        if name in self.clients:
            if self.clients[name] >= amount:
                self.clients[name] -= amount
            else:
                logging.warning("Insufficient funds.")
        else:
            logging.warning("Client not found.")

    def transfer(self, sender, receiver, amount,bank_name):
        if sender in self.clients and receiver in self.clients:
            if self.clients[sender] >= amount:
                self.clients[sender] -= amount
                self.clients[receiver] += amount
            else:
                logging.warning("Insufficient funds, transfer aborted.")
            if self.name != bank_name.name:
                logging.warning("Redirected transfer to your bank but next time set it to correct one.")
        elif self.name == bank_name.name:
            pass
        elif sender in bank_name.clients and receiver in self.clients:
            if bank_name.clients[sender] >= amount:
                bank_name.clients[sender] -= amount
                self.clients[receiver] += amount
            else:
                logging.warning("Insufficient funds, transfer aborted.")
        elif sender in self.clients and receiver in bank_name.clients:
            if self.clients[sender] >= amount:
                self.clients[sender] -= amount
                bank_name.clients[receiver] += amount
            else:
                logging.warning("Insufficient funds, transfer aborted.")
        elif sender in bank_name.clients and receiver in bank_name.clients:
            logging.warning("Both clients are not in this bank, use their bank. Transfer aborted.")
        else:
            logging.warning("Clients not found, transfer aborted.")

    def print_clients(self):
        print("{} clients account statements:".format(self.name))
        for name, balance in self.clients.items():
            print(f"{name}: {balance}")

def main():
    bank = Bank("My Bank")
    bank1 = Bank("My 2nd Bank")
    bank.add_client("Alice", 1000)
    bank.add_client("Bob", 500)
    bank1.add_client("Bryan", 1000)
    bank1.add_client("Cooper", 500)
    bank.print_clients()
    bank.deposit("Alice", 500)
    bank.withdraw("Bob", 200)
    bank.print_clients()
    bank.transfer("Alice", "Bob", 300,bank1)
    bank.print_clients()
    bank1.print_clients()
    bank.transfer("Bryan", "Cooper", 300,bank1)
    bank1.print_clients()

if __name__ == "__main__":
    main()
