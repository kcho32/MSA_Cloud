class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()
        
    def add(self, val):    
        if self.value + val >= 100:
            self.value = 100
        else:
            super().add(val)
    
    
        
    
    



a = MaxLimitCalculator()
a.add(50)
a.add(130)
print(a.value)
