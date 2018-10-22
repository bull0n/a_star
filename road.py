import city

class Road:
    def __init__(self, from_city, to_city, length):
        self.from_city = from_city
        self.to_city = to_city
        self.length = length

    def __str__(self):
        return f'from : {str(self.from_city)} to : {str(self.to_city)} length : {str(self.length)}' 
