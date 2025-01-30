class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s %= 60
        return Time(m, s)

    def __sub__(self, other):
        m = self.minutes - other.minutes
        s = self.seconds - other.seconds
        # m += s // 60
        # s %= 60
        return Time(m, s)

    def __truediv__(self, other):
        #
        m = self.minutes / other.minutes
        s = self.seconds / other.seconds
        # m += s // 60
        # s %= 60
        return Time(m, s)

    def __floordiv__(self, other):
        m = self.minutes // other.minutes
        s = self.seconds // other.seconds
        # m += s // 60
        # s %= 60
        return Time(m, s)

    def __iadd__(self, other):
        """ Сложение двух объектов при += """
        self.minutes += other.minutes
        self.seconds += other.seconds
        self.minutes += self.seconds // 60
        self.seconds %= 60
        return Time(self.minutes, self.seconds)

    def __eq__(self, other):
        """ Для оператора =="""
        pass

    def __lt__(self, other):
        """ Для оператора <"""
        pass

    def __le__(self, other):
        """ Для оператора <="""
        pass

    def __gt__(self, other):
        """ Для оператора >"""
        pass

    def __ge__(self, other):
        """ Для оператора >="""
        pass

    def __ne__(self, other):
        """ Для оператора !="""
        pass

    def __len__(self, other):
        """ Для оператора len"""
        pass

    def __str__(self):
        return f'{self.minutes}:{self.seconds}'





time1 = Time(2, 50)
time2 = Time(1, 45)
time3 = time1 + time2

print(time3)

print(time1 - time2)
print(time1 / time2)
print(time1 // time2)

time1 += time2
print(time1)


