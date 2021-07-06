import sys


class four_calc:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    

    def setdata(self,first,second):
        self.first = first
        self.second = second
    

    def add(self):
        result = self.first + self.second
        return result
    
    
    def subtract(self):
        result = self.first - self.second
        return result
    

    def multiply(self):
        result = self.first * self.second
        return result


    def divide(self):
        result = self.first / self.second
        return result

<<<<<<< HEAD
if len(sys.argv) != 4:
    pass

=======
>>>>>>> daf597275073efc36eeed9af75c71d3292637138
