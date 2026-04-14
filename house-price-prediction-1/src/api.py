from flask import Blueprint, request, jsonify, render_template
import joblib
import pandas as pd
import os
from src.data.india_cities import cities_by_state
from src.data.amenities import amenities_list, bhk_options, facing_options

# -------------------------------
# Load Model
# -------------------------------
# Get the base directory (parent of src)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(base_dir, "models", "house_price_model.pkl")
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"Warning: Could not load model: {e}")
else:
    print(f"Warning: Model file not found at {MODEL_PATH}")

# Suggested locations
POPULAR_LOCATIONS = {
    "budget_low": ["Tambaram", "Avadi", "Perambur"],
    "budget_mid": ["Velachery", "Anna Nagar", "Madipakkam"],
    "budget_high": ["Adyar", "Besant Nagar", "ECR"]
}

# -------------------------------
# API Blueprint
# -------------------------------
api_blueprint = Blueprint("api", __name__)

# -------------------------------
# Home Page Route (moved to blueprint for consistency)
# -------------------------------
@api_blueprint.route("/home", methods=["GET"])
def home():
    return render_template("index.html", result=None, locations=[])

# -------------------------------
# Prediction Route
# -------------------------------
@api_blueprint.route("/predict", methods=["POST"])
def predict():
    print("BACKEND VERSION: NEW (ACTIVE)")   # Debug indicator
    
    if model is None:
        return render_template(
            "index.html",
            result="❌ Model not loaded. Please ensure the model file exists.",
            locations=[]
        )
    
    try:
        Area = float(request.form.get("Area", 0))
        Bedrooms = int(request.form.get("Bedrooms", 0))
        Stories = int(request.form.get("Stories", 0))
        Parking = int(request.form.get("Parking", 0))
        Amenities = request.form.get("Amenities", "")
    except (ValueError, TypeError) as e:
        return render_template(
            "index.html",
            result=f"❌ Invalid input: {str(e)}",
            locations=[]
        )

    # -------------------------------
    # Prepare base input dataframe
    # -------------------------------
    amen_list = [a.strip() for a in Amenities.split(",") if a.strip()]
    amen_count = len(amen_list)

    user_df = pd.DataFrame({
        "Area": [Area],
        "Bedrooms": [Bedrooms],
        "Bathrooms": [1],       # default because UI removed bathrooms
        "Stories": [Stories],
        "Parking": [Parking],
        "amen_count": [amen_count],
        "city_num": [0]
    })

    # -------------------------------
    # Fix: Auto-match all model columns
    # -------------------------------
    try:
        model_cols = list(model.feature_names_in_)  # get columns from trained model
    except:
        model_cols = list(user_df.columns)  # fallback

    # Create a DF with all columns model needs, filled with 0 by default
    final_df = pd.DataFrame(0, index=[0], columns=model_cols)

    # Copy matching user values into final_df
    for col in user_df.columns:
        if col in final_df.columns:
            final_df[col] = user_df[col]

    # -------------------------------
    # Predict
    # -------------------------------
    try:
        pred = model.predict(final_df)[0]
    except Exception as e:
        return render_template(
            "index.html",
            result=f"❌ Prediction Error: {str(e)}",
            locations=[]
        )

    price = float(pred)

    # -------------------------------
    # Suggested locations based on predicted budget
    # -------------------------------
    if price < 3000000:
        suggested = POPULAR_LOCATIONS["budget_low"]
    elif price < 8000000:
        suggested = POPULAR_LOCATIONS["budget_mid"]
    else:
        suggested = POPULAR_LOCATIONS["budget_high"]

    # -------------------------------
    # Render result
    # -------------------------------
    return render_template(
        "index.html",
        result=f"Predicted Price: ₹{price:,.2f}",
        locations=suggested
    )

@api_blueprint.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@api_blueprint.route("/search_properties", methods=["POST"])
def search_properties():
    data = request.get_json() or {}
    
    state = data.get("state", "")
    city = data.get("city", "")
    bhk = data.get("bhk", "")
    sqft_min = data.get("sqft_min", 0)
    sqft_max = data.get("sqft_max", 10000)
    amenities_filter = data.get("amenities", [])
    facing = data.get("facing", "")
    
    # Get available cities for state
    available_cities = cities_by_state.get(state, [])
    
    # Mock search results (replace with DB query later)
    results = {
        "query": {
            "state": state,
            "city": city,
            "bhk": bhk,
            "sqft_range": [sqft_min, sqft_max],
            "amenities": amenities_filter,
            "facing": facing
        },
        "available_cities": available_cities,
        "found_properties": [
            {
                "id": 1,
                "city": city,
                "bhk": bhk,
                "sqft": 800,
                "price": 5000000,
                "amenities": amenities_filter,
                "facing": facing,
                "address": f"Sample property in {city}"
            }
        ] if city in available_cities else [],
        "total_count": 1 if city in available_cities else 0
    }
    
    return jsonify(results)

@api_blueprint.route("/get_states", methods=["GET"])
def get_states():
    states = list(cities_by_state.keys())
    return jsonify({"states": states})

@api_blueprint.route("/get_cities", methods=["GET"])
def get_cities():
    state = request.args.get("state", "")
    cities = cities_by_state.get(state, [])
    return jsonify({"state": state, "cities": cities})

@api_blueprint.route("/get_amenities", methods=["GET"])
def get_amenities():
    return jsonify({"amenities": amenities_list})

@api_blueprint.route("/get_options", methods=["GET"])
def get_options():
    return jsonify({
        "bhk_options": bhk_options,
        "facing_options": facing_options,
        "amenities": amenities_list
    })

@api_blueprint.route("/predict_price", methods=["POST"])
def predict_price():
    data = request.get_json() or {}
    
    sqft = data.get("sqft", 0)
    bhk = data.get("bhk", 1)
    city = data.get("city", "Mumbai")
    amenities = data.get("amenities", [])
    facing = data.get("facing", "east")
    
    # Base price by city (example rates per sqft)
    city_rates = {
        "Mumbai": 250000, "Bangalore": 180000, "Delhi": 200000, "Hyderabad": 120000, "Pune": 150000
    }
    base_rate = city_rates.get(city, 100000)
    
    # Calculate price
    base_price = sqft * base_rate / 1000
    bhk_multiplier = 1 + (bhk - 1) * 0.25
    amenity_bonus = len(amenities) * 50000
    
    predicted_price = int(base_price * bhk_multiplier + amenity_bonus)
    
    return jsonify({
        "predicted_price": predicted_price,
        "details": {
            "city": city,
            "bhk": bhk,
            "sqft": sqft,
            "amenities": amenities,
            "facing": facing
        }
    })
