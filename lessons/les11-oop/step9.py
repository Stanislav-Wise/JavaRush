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

    def __str__(self):
        return f'{self.minutes}:{self.seconds}'



time1 = Time(2, 30)
time2 = Time(1, 45)
time3 = time1 + time2
print(time1 + time2)
print(time3)