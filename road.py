import city
import os

class Road:
    def __init__(self, to_city, length):
        self.to_city = to_city
        self.length = float(length)

    def __str__(self):
        return f'to : %s [length = %s]' % (self.to_city.name, str(self.length))

    def __hash__(self):
        return str(self).__hash__()

    def __eq__(self, compared):
        return self.to_city == compared.to_city and self.length == compared.length
