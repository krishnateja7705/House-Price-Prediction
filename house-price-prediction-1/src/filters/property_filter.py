class PropertyFilter:
    def __init__(self, properties):
        self.properties = properties

    def filter_by_size(self, size):
        return [property for property in self.properties if property.size == size]

    def filter_by_bhk(self, bhk):
        return [property for property in self.properties if property.bhk == bhk]

    def filter_by_price(self, min_price, max_price):
        return [property for property in self.properties if min_price <= property.price <= max_price]

    def filter_by_square_footage(self, min_sqft, max_sqft):
        return [property for property in self.properties if min_sqft <= property.square_footage <= max_sqft]

    def filter_by_facing(self, facing):
        return [property for property in self.properties if property.facing == facing]

    def filter_by_amenities(self, amenities):
        filtered_properties = self.properties
        for amenity in amenities:
            filtered_properties = [property for property in filtered_properties if amenity in property.amenities]
        return filtered_properties

    def apply_filters(self, size=None, bhk=None, min_price=None, max_price=None, min_sqft=None, max_sqft=None, facing=None, amenities=None):
        filtered_properties = self.properties
        
        if size:
            filtered_properties = self.filter_by_size(size)
        if bhk:
            filtered_properties = self.filter_by_bhk(bhk)
        if min_price is not None and max_price is not None:
            filtered_properties = self.filter_by_price(min_price, max_price)
        if min_sqft is not None and max_sqft is not None:
            filtered_properties = self.filter_by_square_footage(min_sqft, max_sqft)
        if facing:
            filtered_properties = self.filter_by_facing(facing)
        if amenities:
            filtered_properties = self.filter_by_amenities(amenities)

        return filtered_properties