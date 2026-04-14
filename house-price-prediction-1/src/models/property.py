class Property:
    def __init__(self, size, price, amenities, location, facing):
        self.size = size  # Size of the property (e.g., 1 BHK, 2 BHK, etc.)
        self.price = price  # Price of the property
        self.amenities = amenities  # List of amenities available
        self.location = location  # Location of the property
        self.facing = facing  # Direction the property faces (e.g., North, South)

    def __repr__(self):
        return f"Property(size={self.size}, price={self.price}, amenities={self.amenities}, location={self.location}, facing={self.facing})"

    def has_amenity(self, amenity):
        return amenity in self.amenities

    def is_within_budget(self, budget):
        return self.price <= budget

    def matches_location(self, desired_location):
        return self.location.lower() == desired_location.lower()

    def matches_facing(self, desired_facing):
        return self.facing.lower() == desired_facing.lower()