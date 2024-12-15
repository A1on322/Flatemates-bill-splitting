class Bill:
    """
    Bill object that contains attributes such as period of bill and amount of bill
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Flatmate object that represents flatmate with such attributes as name of flatmate,
    days_in_house - amount of days that he was in house
    pays(bill) - method that will calculate how much flatmate should pay
    """

    def __init__(self, name, days):
        self.name = name
        self.days_in_house = days

    def pay(self, bill, *args):
        total_days = sum([i.days_in_house for i in args]) + self.days_in_house
        return bill.amount * (self.days_in_house/total_days)
