class Person:

    def __init__(self, name, surname, age, email, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.email = email

    def __repr__(self):
        if self.gender == 'Male':
            return "{} {} - {}".format(self.name, self.surname, self.age)
        else:
            return "{} {}".format(self.name, self.surname)

    def add_age(self, n=1):
        self.age += n


class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTH_NAMES = ['', "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                   "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def add_year(self, n):
        self.year += n

    def add_month(self, n):
        self.add_year((self.month + n - 1) // 12)
        self.month = (self.month + n - 1) % 12 + 1

    def add_day(self, n):
        self.add_month((self.day + n - 1) // 30)
        self.day = (self.day + n - 1) % 30 + 1

    def __repr__(self):
        return "{} {} {}".format(self.day, self.MONTH_NAMES[self.month], self.year)


from exceptions import TimeTypeError, TimeValueError


class Time:
    def __init__(self, hour, minute, second):
        try:
            if type(hour) != int:
                raise TimeTypeError("hour", hour)
            elif type(minute) != int:
                raise TimeTypeError("minute", minute)
            elif type(second) != int:
                raise TimeTypeError("second", second)

            if hour < 0 or hour > 23:
                raise TimeValueError("hour", hour)
            elif minute < 0 or minute > 59:
                raise TimeValueError("minute", minute)
            elif second < 0 or second > 59:
                raise TimeValueError("second", second)

        except TimeValueError as err:
            print(err)
        except TimeTypeError as err:
            print(err)
        else:
            self.hour = hour
            self.minute = minute
            self.second = second

    def __repr__(self):
        try:
            return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
        except AttributeError:
            return "Object is empty."

    def add_hour(self, n):
        try:
            if type(n) != int:
                raise TimeTypeError("param n", n)
            if n <= 0:
                raise TimeValueError("param n", n)
            self.hour = (self.hour + n) % 24
        except TimeValueError as err:
            print(err)
        except TimeTypeError as err:
            print(err)
        except AttributeError:
            print("Object does not have attribute 'hour'.")


class DateTime(Date, Time):
    def __init__(self, year, month, day, hour, minute, second):
        Date.__init__(self, year, month, day)
        Time.__init__(self, hour, minute, second)

    def __repr__(self):
        return "{} {}".format(Date.__repr__(self), Time.__repr__(self))


class Money:
    EXCHANGE_RATE = {"AMD": 1, "RUB": 4, "USD": 400, "EUR": 420}

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return "{} {}".format(self.amount, self.currency)

    def exchange(self, curr):
        rate = Money.EXCHANGE_RATE[self.currency] / Money.EXCHANGE_RATE[curr]
        return Money(curr, rate * self.amount)

    def __add__(self, other):
        if self.currency != other.currency:
            other = other.exchange(self.currency)
        return Money(self.currency, self.amount + other.amount)

    def deposite(self, p, n):
        return Money(self.currency, round(self.amount * ((1 + p / 100) ** n), 2))

    def __mul__(self, n):
        return Money(self.currency, self.amount * n)

