def get_all_properties(connection):
    query = "SELECT * FROM properties"
    cursor = connection.cursor()
    cursor.execute(query)
    properties = cursor.fetchall()
    cursor.close()
    return properties

def get_properties_by_city(connection, city):
    query = "SELECT * FROM properties WHERE city = %s"
    cursor = connection.cursor()
    cursor.execute(query, (city,))
    properties = cursor.fetchall()
    cursor.close()
    return properties

def get_properties_by_amenities(connection, amenities):
    query = "SELECT * FROM properties WHERE amenities && %s"
    cursor = connection.cursor()
    cursor.execute(query, (amenities,))
    properties = cursor.fetchall()
    cursor.close()
    return properties

def get_properties_by_bhk(connection, bhk):
    query = "SELECT * FROM properties WHERE bhk = %s"
    cursor = connection.cursor()
    cursor.execute(query, (bhk,))
    properties = cursor.fetchall()
    cursor.close()
    return properties

def get_properties_by_price_range(connection, min_price, max_price):
    query = "SELECT * FROM properties WHERE price BETWEEN %s AND %s"
    cursor = connection.cursor()
    cursor.execute(query, (min_price, max_price))
    properties = cursor.fetchall()
    cursor.close()
    return properties

def get_properties_by_size(connection, min_size, max_size):
    query = "SELECT * FROM properties WHERE size BETWEEN %s AND %s"
    cursor = connection.cursor()
    cursor.execute(query, (min_size, max_size))
    properties = cursor.fetchall()
    cursor.close()
    return properties

def get_properties_by_facing(connection, facing):
    query = "SELECT * FROM properties WHERE facing = %s"
    cursor = connection.cursor()
    cursor.execute(query, (facing,))
    properties = cursor.fetchall()
    cursor.close()
    return properties