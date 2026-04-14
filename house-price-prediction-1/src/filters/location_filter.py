class LocationFilter:
    def __init__(self, properties):
        self.properties = properties

    def filter_by_city(self, city):
        return [property for property in self.properties if property['city'].lower() == city.lower()]

    def filter_by_state(self, state):
        return [property for property in self.properties if property['state'].lower() == state.lower()]

    def filter_by_location(self, city=None, state=None):
        if city:
            return self.filter_by_city(city)
        elif state:
            return self.filter_by_state(state)
        return self.properties

    def filter_by_multiple_locations(self, cities):
        return [property for property in self.properties if property['city'].lower() in [c.lower() for c in cities]]