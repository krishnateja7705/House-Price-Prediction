def calculate_price_range(min_price, max_price):
    return {"min_price": min_price, "max_price": max_price}

def filter_properties_by_size(properties, size):
    return [property for property in properties if property.size == size]

def filter_properties_by_amenities(properties, amenities):
    filtered_properties = []
    for property in properties:
        if all(amenity in property.amenities for amenity in amenities):
            filtered_properties.append(property)
    return filtered_properties

def sort_properties(properties, sort_by='price', ascending=True):
    return sorted(properties, key=lambda x: getattr(x, sort_by), reverse=not ascending)

def format_property_details(property):
    return {
        "id": property.id,
        "size": property.size,
        "price": property.price,
        "amenities": property.amenities,
        "location": property.location,
        "facing": property.facing
    }