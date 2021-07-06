class Calculator():
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def __init__(self):
        super().__init__()
    
    def minus(self, val):
        self.value -= val
        return self.value


a = UpgradeCalculator()
print(a.add(4))
print(a.minus(2))