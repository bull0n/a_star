class City:
    '''
    Class that represents a city
    composed by a name, coordinates and a dictionnary of connected cities
    the dictionnary make the road directionnal, like in real life. Not every roads are bidirectionnal
    '''
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.connected_cities = {}

    def __str__(self):
        return '%s [%s:%s] connected to\n%s' % (
            self.name,
            self.coordinates[0],
            self.coordinates[1],
            {city.name : str(length) for city, length in self.connected_cities.items()}
        )

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, compared):
        if compared == None:
            return False

        return self.name == compared.name


    def connect_road(self, city, length):
        self.connected_cities[city] = float(length)

    def x(self):
        return float(self.coordinates[0])

    def y(self):
        return float(self.coordinates[1])
