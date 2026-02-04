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
        if val == self.value1*self.value2:
            self.score += 1
            return True
        return False
    
    def get_score(self):
        return self.score
