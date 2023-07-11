from info import Person, Date, Money


class BankAccount:
    def __init__(self, name, surname, age, email, gender, currency, amounth, year, month, day):

        self.owner = Person(name, surname, age, email, gender)
        self.balance = Money(currency, amounth)
        self.created_at = Date(year, month, day)

    def __repr__(self):
        return "{}, Balance-{}, {}".format(self.owner, self.balance, self.created_at)

k = BankAccount("Aram", "Aramyan", 20, "aram@mail.com", "Male", "AMD", 250, 2023, 10, 20)
print(k)
print(k.balance.exchange("USD"))
k.created_at.add_day(-1)
print(k.created_at)
k.owner.add_age(5)
print(k.owner)
