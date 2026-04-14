# House Price Prediction Project

This project is designed to provide a comprehensive house price prediction service for users looking to search for houses or apartments across various cities in India. The application allows users to filter properties based on various criteria, including amenities, size, and location.

## Project Structure

The project is organized as follows:

```
house-price-prediction
├── src
│   ├── api.py                # API endpoints for property search and price prediction
│   ├── main.py               # Main entry point of the application
│   ├── config.py             # Configuration settings for the application
│   ├── models
│   │   ├── __init__.py       # Initializes the models package
│   │   ├── price_predictor.py # Class for predicting house prices
│   │   └── property.py        # Class representing a property
│   ├── database
│   │   ├── __init__.py       # Initializes the database package
│   │   ├── db_connection.py   # Manages database connections
│   │   └── queries.py         # Functions for executing database queries
│   ├── data
│   │   ├── __init__.py       # Initializes the data package
│   │   ├── india_cities.py   # List of major cities in India
│   │   └── amenities.py       # List of available amenities
│   ├── filters
│   │   ├── __init__.py       # Initializes the filters package
│   │   ├── amenity_filter.py  # Filters properties based on amenities
│   │   ├── property_filter.py  # Filters properties based on size and price
│   │   └── location_filter.py  # Filters properties based on location
│   ├── utils
│   │   ├── __init__.py       # Initializes the utils package
│   │   └── helpers.py        # Utility functions for data processing
│   └── templates
│       ├── index.html        # Main HTML template
│       ├── search.html       # Search page template
│       └── results.html      # Results display template
├── data
│   ├── raw
│   │   └── india_properties.csv # Raw property data
│   └── processed
│       └── cleaned_properties.csv # Processed property data
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
└── README.md                  # Project documentation
```

## Features

- **Search Properties**: Users can search for properties in all major cities across India.
- **Filter Options**: Users can filter properties based on:
  - Amenities (e.g., pool, gym, park)
  - Property size (1 BHK to 5 BHK)
  - Square footage
  - Location preferences
- **Price Prediction**: The application provides price predictions based on various input features.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd house-price-prediction
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your database credentials and any other necessary configuration.

4. **Run the Application**:
   Start the application by running:
   ```
   python src/main.py
   ```

5. **Access the Application**:
   Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage Guidelines

- Use the search page to input your preferences for properties.
- Apply filters to narrow down your search results.
- View detailed results and price predictions for selected properties.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.