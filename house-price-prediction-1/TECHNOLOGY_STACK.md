# House Price Prediction Project - Technology Stack & Components

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Core Technologies](#core-technologies)
3. [Web Framework & API](#web-framework--api)
4. [Machine Learning Stack](#machine-learning-stack)
5. [Data Processing Libraries](#data-processing-libraries)
6. [Database & ORM](#database--orm)
7. [Project Architecture](#project-architecture)
8. [Key Components Explained](#key-components-explained)

---

## 🎯 Project Overview

This is a **House Price Prediction Web Application** built using Python that allows users to:
- Predict house prices based on property features (Area, Bedrooms, Stories, Parking, Amenities)
- Search and filter properties across Indian cities
- Get location suggestions based on predicted budget
- Access a RESTful API for property-related operations

---

## 🔧 Core Technologies

### 1. **Python 3.x**
- **Purpose**: Primary programming language
- **Usage**: Backend development, data processing, machine learning model training
- **Why**: Python's extensive libraries for ML, web development, and data science

---

## 🌐 Web Framework & API

### 2. **Flask (v2.3.0+)**
- **Purpose**: Lightweight web framework for building the web application
- **Key Features Used**:
  - **Routing**: `@app.route()` decorators for URL routing
  - **Templates**: Jinja2 template engine for HTML rendering
  - **Request Handling**: `request.form.get()` for form data processing
  - **JSON Responses**: `jsonify()` for API responses
  - **Blueprints**: Modular route organization (`api_blueprint`)
- **Usage in Project**:
  ```python
  # Main application setup
  app = Flask(__name__, template_folder=template_dir)
  app.register_blueprint(api_blueprint, url_prefix="/api")
  
  # Route handling
  @app.route("/")
  @app.route("/predict", methods=["POST"])
  ```
- **Why Flask**: Lightweight, flexible, perfect for ML model serving

### 3. **Flask-CORS (v4.0.0+)**
- **Purpose**: Handle Cross-Origin Resource Sharing (CORS)
- **Usage**: Allows frontend to make API calls from different domains
- **Why**: Essential for web applications with separate frontend/backend

### 4. **FastAPI (v0.100.0+)** & **Uvicorn (v0.23.0+)**
- **Purpose**: Alternative async web framework (included but Flask is primary)
- **FastAPI Features**: 
  - Type hints for request validation
  - Automatic API documentation
  - Async support
- **Uvicorn**: ASGI server for running FastAPI applications
- **Note**: Project primarily uses Flask, but FastAPI is available for future async needs

### 5. **Jinja2 (v3.1.0+)**
- **Purpose**: Template engine for Flask
- **Usage**: Dynamic HTML generation with template variables
- **Example**:
  ```python
  render_template("index.html", result=price, locations=suggested)
  ```

---

## 🤖 Machine Learning Stack

### 6. **Scikit-learn (v1.3.0+)**
- **Purpose**: Machine learning library for model training and evaluation
- **Key Components Used**:
  - **`LinearRegression`**: Regression model for price prediction
  - **`train_test_split`**: Data splitting for training/validation
  - **`mean_squared_error`**: Model evaluation metric (RMSE calculation)
  - **`r2_score`**: Coefficient of determination for model accuracy
- **Usage in Project**:
  ```python
  from sklearn.linear_model import LinearRegression
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import mean_squared_error, r2_score
  
  # Model training
  model = LinearRegression()
  model.fit(X_train, y_train)
  
  # Evaluation
  rmse = np.sqrt(mean_squared_error(y_test, y_pred))
  r2 = r2_score(y_test, y_pred)
  ```
- **Why**: Industry-standard ML library with robust algorithms

### 7. **Joblib (v1.3.0+)**
- **Purpose**: Efficient serialization for Python objects (especially NumPy arrays)
- **Usage**: 
  - **Saving trained models**: `joblib.dump(model, "model.pkl")`
  - **Loading models**: `joblib.load("model.pkl")`
  - **Saving feature columns**: Persisting model feature names for prediction
- **Why**: Faster than pickle for large NumPy arrays, essential for ML model persistence

### 8. **NumPy (v1.24.0+)**
- **Purpose**: Numerical computing library
- **Usage**:
  - Mathematical operations on arrays
  - RMSE calculation: `np.sqrt(mean_squared_error(...))`
  - Data manipulation and transformation
- **Why**: Foundation for all numerical operations in ML

---

## 📊 Data Processing Libraries

### 9. **Pandas (v2.0.0+)**
- **Purpose**: Data manipulation and analysis library
- **Key Features Used**:
  - **DataFrames**: Primary data structure for handling CSV data
  - **`read_csv()`**: Loading house price dataset
  - **`get_dummies()`**: One-hot encoding for categorical variables (State, City)
  - **DataFrame operations**: Feature engineering, column manipulation
- **Usage in Project**:
  ```python
  # Loading data
  data = pd.read_csv("data/house_prices.csv")
  
  # Feature encoding
  X = pd.get_dummies(X, drop_first=True)
  
  # Creating prediction DataFrame
  user_df = pd.DataFrame({
      "Area": [Area],
      "Bedrooms": [Bedrooms],
      "Stories": [Stories],
      "Parking": [Parking],
      "amen_count": [amen_count]
  })
  ```
- **Why**: Essential for data preprocessing and feature engineering

---

## 🗄️ Database & ORM

### 10. **SQLAlchemy (v2.0.0+)**
- **Purpose**: SQL toolkit and Object-Relational Mapping (ORM) library
- **Usage**:
  - Database connection management
  - ORM for property data models
  - Query building for property searches
- **Implementation**:
  ```python
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker
  
  engine = create_engine(DATABASE_URL)
  Session = sessionmaker(bind=engine)
  ```
- **Why**: Provides database abstraction and easy querying

### 11. **python-dotenv (v1.0.0+)**
- **Purpose**: Load environment variables from `.env` file
- **Usage**: Secure storage of database credentials, API keys
- **Why**: Best practice for configuration management

---

## 🌍 HTTP & API Libraries

### 12. **Requests (v2.31.0+)**
- **Purpose**: HTTP library for making API calls
- **Usage**: External API integration (if needed for property data)
- **Why**: Simple and powerful HTTP client

---

## 🏗️ Project Architecture

### **MVC (Model-View-Controller) Pattern**

#### **Models** (`src/models/`)
- **`price_predictor.py`**: PricePredictor class for model loading and prediction
- **`property.py`**: Property data model class

#### **Views** (`src/templates/`)
- **`index.html`**: Main prediction interface with form
- **`search.html`**: Property search page
- **`results.html`**: Search results display

#### **Controllers** (`src/`)
- **`main.py`**: Flask application factory and main routes
- **`api.py`**: API blueprint with REST endpoints

### **Project Structure**

```
house-price-prediction-1/
├── src/
│   ├── main.py              # Flask app entry point
│   ├── api.py              # API routes and endpoints
│   ├── config.py           # Configuration settings
│   ├── model_training.py   # ML model training script
│   ├── predict.py         # Prediction logic
│   ├── data_preprocessing.py  # Data cleaning/transformation
│   ├── models/            # ML model classes
│   ├── database/          # Database connection & queries
│   ├── filters/           # Property filtering logic
│   ├── data/              # Static data (cities, amenities)
│   ├── templates/         # HTML templates
│   └── utils/             # Helper functions
├── data/
│   └── house_prices.csv   # Training dataset (100 cities)
├── models/
│   ├── house_price_model.pkl  # Trained ML model
│   └── model_columns.pkl      # Feature column names
└── requirements.txt       # Python dependencies
```

---

## 🔑 Key Components Explained

### **1. Model Training Pipeline** (`model_training.py`)

**Process**:
1. **Load Data**: Read CSV file with house prices
2. **Feature Engineering**: 
   - Drop target variable (Price)
   - One-hot encode categorical features (State, City)
3. **Data Splitting**: 80% training, 20% testing
4. **Model Training**: Train LinearRegression model
5. **Evaluation**: Calculate RMSE and R² score
6. **Persistence**: Save model and feature columns using Joblib

**Metrics**:
- **RMSE**: Root Mean Squared Error (lower is better)
- **R² Score**: Coefficient of determination (1.0 = perfect prediction)

### **2. Prediction API** (`api.py`)

**Endpoints**:
- **`POST /api/predict`**: Main prediction endpoint
- **`POST /api/search_properties`**: Property search with filters
- **`GET /api/get_states`**: Get list of Indian states
- **`GET /api/get_cities`**: Get cities for a state
- **`GET /api/get_amenities`**: Get available amenities
- **`GET /api/health`**: Health check endpoint

**Prediction Flow**:
1. Receive form data (Area, Bedrooms, Stories, Parking, Amenities)
2. Process amenities (count amenities)
3. Create DataFrame with user inputs
4. Match columns with trained model features
5. Fill missing columns with zeros
6. Generate prediction using loaded model
7. Suggest locations based on predicted price

### **3. Data Preprocessing** (`data_preprocessing.py`)

**Functions**:
- **`load_data()`**: Load CSV dataset
- **`preprocess_data()`**: 
  - Remove non-numeric columns (State, City)
  - Separate features (X) and target (y)
  - Split into train/test sets

### **4. Feature Engineering**

**Numeric Features**:
- **Area**: Square footage of property
- **Bedrooms**: Number of bedrooms
- **Bathrooms**: Number of bathrooms (defaulted to 1)
- **Stories**: Number of floors
- **Parking**: Number of parking spaces
- **amen_count**: Count of amenities

**Categorical Features** (One-hot encoded):
- **State**: Indian state (Maharashtra, Karnataka, etc.)
- **City**: City name (Mumbai, Bengaluru, etc.)

### **5. Model Persistence**

**Saved Files**:
- **`house_price_model.pkl`**: Trained LinearRegression model
- **`model_columns.pkl`**: List of feature column names

**Why Both?**: 
- Model needs feature names to ensure correct column order during prediction
- Prevents column mismatch errors when making predictions

### **6. Web Interface** (`templates/index.html`)

**Features**:
- **Glassmorphism UI**: Modern glass-effect design
- **Form Inputs**: Area, Bedrooms, Stories, Parking, Amenities
- **Real-time Prediction**: Submit form to get price prediction
- **Location Suggestions**: Shows recommended areas based on budget
- **Responsive Design**: Works on desktop and mobile

### **7. Database Integration** (`database/`)

**Components**:
- **`db_connection.py`**: SQLAlchemy engine and session management
- **`queries.py`**: Database query functions for property search

**Note**: Currently uses mock data, but structure is ready for real database integration

---

## 📈 Machine Learning Model Details

### **Algorithm**: Linear Regression

**Why Linear Regression?**:
- Simple and interpretable
- Fast training and prediction
- Works well for continuous target variables (price)
- Good baseline model for regression tasks

**Model Input Features**:
- Numeric: Area, Bedrooms, Bathrooms, Stories, Parking, amen_count
- Encoded: State_*, City_* (one-hot encoded)

**Model Output**:
- Predicted house price in Indian Rupees (₹)

**Prediction Process**:
```python
# 1. Load model
model = joblib.load("models/house_price_model.pkl")

# 2. Prepare input DataFrame
user_df = pd.DataFrame({...})

# 3. Match model columns
final_df = pd.DataFrame(0, index=[0], columns=model_cols)
for col in user_df.columns:
    if col in final_df.columns:
        final_df[col] = user_df[col]

# 4. Predict
predicted_price = model.predict(final_df)[0]
```

---

## 🎨 Frontend Technologies

### **HTML5 & CSS3**
- Modern semantic HTML
- CSS Grid and Flexbox for layout
- Custom styling with glassmorphism effects
- Responsive design principles

### **JavaScript** (if used in templates)
- Form validation
- AJAX requests to API endpoints
- Dynamic content updates

---

## 🔐 Security & Configuration

### **Environment Variables** (`.env`)
- Database credentials
- API keys
- Debug mode settings
- Port configuration

### **Configuration** (`config.py`)
- Database URI
- API keys
- Debug mode
- Allowed hosts
- Port number

---

## 📦 Data Management

### **Dataset** (`data/house_prices.csv`)
- **100 Indian cities** with property data
- **Features**: State, City, Area, Bedrooms, Stories, Parking, Price
- **Price Range**: 25 lakhs to 3 crores (₹2,500,000 - ₹30,000,000)
- **All Metro Cities Included**: Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune, Ahmedabad

---

## 🚀 Deployment Considerations

### **Development**:
- Flask development server (`debug=True`)
- Local file-based model storage

### **Production Ready**:
- WSGI server (Gunicorn) for Flask
- Environment-based configuration
- Database integration ready
- API endpoints for frontend consumption

---

## 📝 Summary

This project demonstrates a **complete ML-powered web application** using:
- **Flask** for web framework
- **Scikit-learn** for machine learning
- **Pandas** for data processing
- **Joblib** for model persistence
- **SQLAlchemy** for database operations
- **Jinja2** for templating

The architecture follows **best practices** with:
- Modular code organization
- Separation of concerns (MVC pattern)
- API-first design
- Model persistence and versioning
- Comprehensive error handling

---

## 🔄 Workflow

1. **Data Collection** → CSV file with 100 cities
2. **Data Preprocessing** → Clean and encode features
3. **Model Training** → Train LinearRegression model
4. **Model Persistence** → Save model using Joblib
5. **Web Application** → Flask app serves predictions
6. **API Endpoints** → RESTful API for predictions and searches
7. **User Interface** → HTML forms for user input
8. **Prediction** → Real-time price prediction based on inputs

---

*This document provides a comprehensive overview of all technologies, libraries, and components used in the House Price Prediction project.*

