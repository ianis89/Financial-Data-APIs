#PART 1
# create classes for geometrical forms'
# triangle, square, rectangle
# all objects need to know how many lines it has and how long is each line
# they must have a method to compute the area and perimeter

import abc
import math

# public -> from anywhere
# protected -> only from class and its children (and nephews and so on), declare with _
# private -> only from the class, declare with __ in front
from abc import abstractmethod, ABC


# an abstract class is a class which cannot be instantiated
class GeometricalForm(abc.ABC):
    def __init__(self, lines: list[float]):
        self._lines = lines  # this is a protected variable
        self.__private_var = True  # this is a private variable

    def perimeter(self) -> float:  # this is a public method
        return sum(self._lines)

    @abstractmethod  # called decorator, abstract method imposes implementation on children
    def area(self) -> float:
        pass

    def __private_method(self):
        pass


class Triangle(GeometricalForm):
    def __init__(self, line1: float, line2: float, line3: float):
        super().__init__([line1, line2, line3])

    def area(self):
        sp = self.perimeter() / 2  # semiperimeter
        return math.sqrt(sp * (sp - self._lines[0]) * (sp - self._lines[1]) * (sp - self._lines[2]))


class Rectangle(GeometricalForm):
    def __init__(self, length: float, width: float):
        super().__init__([length, length, width, width])

    def area(self) -> float:
        return self._lines[0] * self._lines[2]


class Square(Rectangle):
    def __init__(self, line: float):
        super().__init__(line, line)


if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    print("triangle p", t.perimeter())
    print("triangle area", t.area())
    d = Rectangle(5, 7)
    print("rectangle p", d.perimeter())
    print("rectangle area", d.area())
    s = Square(1)
    print("square p", s.perimeter())
    print("square area", s.area())







# PART 2

# create a bank account class, will contain the account number, owner's name & balance
# add methods to withdraw & deposit & to check the balance
"""
Module Docstring (a description of your program goes here)
"""
class BankAccount:
    """
    BankAccount Class
    """
    def __init__(self, name: str):
        self.name = name
        self.balance = 0

    def deposit(self, amount: float) -> bool:
        '''adds money to balance'''
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        '''subtracts money from balance if funds are sufficient'''
        if amount > self.balance or amount < 0:
            return False
        self.balance -= amount
        return True

    def display_balance(self):
        """ displays current account balance """
        print(f'\nNet Available Balance is ${self.balance}')

def interface():
    """
    Interface for interacting with the bank account
    """
    print(f'Hello! Welcome to the Deposit and Withdrawal Machine {name}!')
    while True:
        action = input('\nWould you like to deposit (D), withdraw (W), show balance (S), or exit (E)? ').upper()

        if action in "DWSE":
            if action == "D":
                try:
                    deposit_amount = float(input("How much would you like to deposit: "))
                    if not account.deposit(deposit_amount):
                        print("Please enter a positive number!")
                    else:
                        print(f"Successfully deposited {deposit_amount} into your account.")
                except ValueError:
                    print("Please enter a positive number.")
            if action == "W":
                try:
                    withdraw_amount = float(input("How much would you like to withdraw: "))
                    if not account.withdraw(withdraw_amount):
                        print("You do not have enough money to withdraw.")
                    else:
                        print(f"Successfully withdraw {withdraw_amount} from your account.")
                except ValueError:
                    print("Please enter a positive number.")
            if action == "S":
                account.display_balance()
            if action == "E":
                break

if __name__ == '__main__':
    name = input('What is your name? ')
    account = BankAccount(name)
    interface()

# PART 3

# create a class which represent a deck of cards (poker or cruce)
# we have a method to receive a specified number of cards
# we have a method to put all the cards back in the deck
import random
class PockerDeck:
    def __init__(self):
        self.put_cards_back()

    def put_cards_back(self):
        self.cards = {
            "trefla": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
            "inima rosie": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
            "romb": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
            "inima neagra": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
        }

    def get_cards(self, number_of_cards: int):
        cards = []
        for i in range(0, number_of_cards):
            extracted_card = self.__extract_one_card()
            cards.append(extracted_card)
        return cards

    def __extract_one_card(self):
        # TODO optimize, remove duplicate code
        random_colour = random.choice(["trefla", "inima rosie", "romb", "inima neagra"])
        random_number = random.choice(self.cards[random_colour])
        self.cards[random_colour].remove(random_number)
        return random_colour, random_number


if __name__ == "__main__":
    deck = PockerDeck()
    cards = deck.get_cards(5)
    print(cards)
    cards = deck.get_cards(2)
    print(cards)
    print(deck.cards)
    deck.put_cards_back()
    print(deck.cards)