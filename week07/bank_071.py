#!/usr/bin/env python3

class BankAccount:
    def __init__(self, balance=0):
        self.bal = float(balance)

    def deposit(self, ammount):
        self.bal = self.bal + ammount

    def withdraw(self, ammount):
        if self.bal < ammount:
            print('Insufficient funds available')
        else:
            self.bal = self.bal - ammount

    def print_details(self):
        print(f'Your current balance is: {self.bal:.2f} euro')
