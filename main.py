1-m
class PhoneBattery:
    def __init__(self, parcent):
        self.parcent = parcent

    def use(self, amount):
        self.amount = amount
        print(f"Batareya: {self.amount}%")

    def charge(self):
        print(f"Quvvat tushdi")

u1 = PhoneBattery("Iphone")

u1.use(40)

u1.charge()
