class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.connected_roads = []

    def __str__(self):
        return f'{self.name} [{str(self.coordinates[0])}:{str(self.coordinates[1])}] connected to : {[str(road) for road in self.connected_roads]}'

    def __hash__(self):
        return str(self).__hash__()

    def __eq__(self, compared):
        if type(compared) == str:
            return self.name == compared
        else :
            return self.name == compared.name and self.coordinates == compared.coordinates


    def connect_road(self, road):
        self.connected_roads.append(road)

    def x(self):
        return self.coordinates[0]

    def y(self):
        return self.coordinates[1]
