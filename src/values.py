from random import randint

class ValueManager:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.score = 0

    def randomize(self):
        self.value1 = randint(-10, 10)
        self.value2 = randint(-10, 10)
        return [self.value1, self.value2]

    def check(self, val):
        val == (self.value1*self.value2)
        if(val):
            self.score += 1
        return val
    
    def get_score(self):
        return self.score