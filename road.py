import city

class Road:
    def __init__(self, to_city, length):
        self.to_city = to_city
        self.length = float(length)

    def __str__(self):
        return f'to : {self.to_city.name} [length = {str(self.length)}]'
