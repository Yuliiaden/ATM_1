class AttemptsOver(Exception): #оконченные попытки
    pass


class AtmBalance(Exception): # баланс
    pass


class EnterPin(Exception): #ввод пина
    pass


class IncorrectPin(Exception):   #неправильный пин
    pass


class Atm():
    atm_balance = 10000
    attempts = 2
    client_can_get_money = False

    def rise_money(self, rise_money):
        """Method to add some money to the ATM"""
        return self.atm_balance + rise_money

    def enter_pin(self, pin):
        """Method to check pin"""
        correct_pin = 777

        if self.attempts == 0:
            raise AttemptsOver("Attempts are over!!!")

        if pin != correct_pin:
            self.attempts = self.attempts - 1
            raise IncorrectPin("Incorrect Pin!!!")

        if correct_pin == pin:
            self.client_can_get_money = True
            return True

    def get_money(self, money):
        """Method to get some money for sweets from the ATM"""
        if self.client_can_get_money:
            if money <= self.atm_balance:
                self.atm_balance = self.atm_balance - money
                return money
            else:
                raise AtmBalance("Atm balance is no enough!!!")
        raise EnterPin("Enter pin first!!!")

    def check_balance(self):
        """Method to check ATM balance"""
        if self.client_can_get_money:
            return self.atm_balance

        raise EnterPin("Enter pin first!!!")
