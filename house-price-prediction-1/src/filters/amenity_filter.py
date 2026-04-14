class AmenityFilter:
    def __init__(self, properties):
        self.properties = properties

    def filter_by_amenities(self, selected_amenities):
        filtered_properties = []
        for property in self.properties:
            if all(amenity in property['amenities'] for amenity in selected_amenities):
                filtered_properties.append(property)
        return filtered_properties

    def filter_by_single_amenity(self, amenity):
        return [property for property in self.properties if amenity in property['amenities']]