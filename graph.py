from road import Road
from city import City

import sys

class Graph:
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        '''
        add a city in our graph
        '''
        self.cities.append(city)

    def add_road(self, from_city, to_city, length):
        '''
        add a road connecting 2 city in our graph
        '''
        from_city.connect_road(Road(to_city, length))
        to_city.connect_road(Road(from_city, length))

    def search_city(self, city_name):
        '''
        return a city by its name
        '''
        for city in self.cities:
            if city == city_name:
                return city
        raise Exception('city not found')


    def a_star(self, from_city, to_city, heuristic):
        '''
        find the shortest path between 2 city
        return an array of roads
        '''
        history = set()
        to_visit = {from_city}

        dict_h = {}
        dict_g = {}
        dict_h[from_city] = heuristic(from_city, to_city)
        dict_g[from_city] = 0

        while to_visit:
            current = self.smallest_h(dict_h)

            to_visit.remove(current)
            history.add(current)

            for road in current.connected_roads:
                if not road.to_city in history:
                    temp_g = dict_g[current] + road.length

                    if not road.to_city in to_visit:
                        to_visit.add(current)
                    else:
                        if temp_g < dict_g[road.to_city]:
                            dict_g[road.to_city] = temp_g
                            dict_h[road.to_city] = dict_g[road.to_city] + heuristic(road.to_city, to_city)



    def smallest_h(self, d):
        min = None

        for key, val in d.items():
            if min == None:
                min = key
            else:
                if dic[min] > val:
                    min = key
        return min


    def __str__(self):
        return f'cities : {[str(city) for city in self.cities]}'
