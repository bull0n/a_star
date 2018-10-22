from road import Road
from city import City

class Graph:
    def __init__(self):
        self.cities = []
        self.roads = []

    def add_city(self, city):
        self.cities.append(city)

    def add_road(self, road):
        self.roads.append(road)

    def search_city(self, city_name):
        for city in self.cities:
            if city == city_name:
                return city
        raise Exception('city not found')

    def __str__(self):
        return f'cities : {[str(city) for city in self.cities]} roads : {[str(road) for road in self.roads]}'
