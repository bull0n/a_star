from road import Road
from city import City

import sys
import os
import math

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
        from_city.connect_road(to_city, length)
        to_city.connect_road(from_city, length)

    def search_city(self, city_name):
        '''
        return a city by its name
        '''
        for city in self.cities:
            if city == city_name:
                return city
        raise Exception('city not found')


    def a_star(self, from_city, to_city, heuristic, debug = True, display_iterations = True):
        '''
        find the shortest path between 2 city
        return an array of roads
        '''

        if debug:
            print('\n')

        iterations = 0

        history = set() # cities already visited
        to_visit = {from_city} # cities not visited yet

        dict_h = {city: math.inf for city in self.cities} # initialize a dict with a really high value for every cities in the graph
        dict_g = {}

        path_done = {}
        current = None

        dict_h[from_city] = heuristic(from_city, to_city)
        dict_g[from_city] = 0

        while to_visit:
            current = self.smallest_h(dict_h, to_visit)

            if debug:
                print(f'visiting : {current.name}')

            if current == to_city:
                break

            to_visit.remove(current)
            history.add(current)

            for city, length in current.connected_cities: # check all neighbors
                if not city in history: # if in history, ignore it
                    temp_g = dict_g[current] + length # calculate the temporary g

                    if not city in to_visit: # if the city isn't in the visit map yet add it
                        to_visit.add(city)
                        if debug:
                            print(f'discovered new city ; {city.name}')
                    elif temp_g >= dict_g[city]: # if the city has a better distance, add its better value
                        if debug:
                            print(f'visiting {city.name} but distance is not optimal')
                        continue


                    path_done[city] = current
                    dict_g[city] = temp_g
                    dict_h[city] = dict_g[city] + heuristic(city, to_city)

                    if debug:
                        print(f'new shorter path to {city.name} - distance : {dict_h[city]}')
            if display_iterations:
                iterations += 1

        if display_iterations:
            print(f'\niterations : {iterations}\n')

        return self.reconstruct_path(path_done, current)

    def reconstruct_path(self, path_done, current):
        '''
        iterate over the map build to build the final path
        '''
        final_path = [current]

        while current in path_done.keys():
            current = path_done[current]
            final_path.append(current)
        return final_path

    def smallest_h(self, d, to_visit):
        min = None

        for key, val in d.items():
            if key in to_visit:
                if min == None:
                    min = key
                else:
                    if d[min] > val:
                        min = key
        return min


    def __str__(self):
        return f'cities :\n%s' % '\n'.join([str(city)+os.linesep for city in self.cities])
