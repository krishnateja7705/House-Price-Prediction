from flask import Flask, jsonify, render_template, request
from src.api import api_blueprint, model, POPULAR_LOCATIONS
import os
import joblib
import pandas as pd

def create_app():
    # Get the base directory (parent of src)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, "src", "templates")
    
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    
    @app.route("/")
    def index():
        return render_template("index.html", result=None, locations=[])
    
    @app.route("/predict", methods=["POST"])
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

        # Prepare base input dataframe
        amen_list = [a.strip() for a in Amenities.split(",") if a.strip()]
        amen_count = len(amen_list)

        user_df = pd.DataFrame({
            "Area": [Area],
            "Bedrooms": [Bedrooms],
            "Bathrooms": [1],
            "Stories": [Stories],
            "Parking": [Parking],
            "amen_count": [amen_count],
            "city_num": [0]
        })

        # Auto-match all model columns
        try:
            model_cols = list(model.feature_names_in_)
        except:
            model_cols = list(user_df.columns)

        final_df = pd.DataFrame(0, index=[0], columns=model_cols)
        for col in user_df.columns:
            if col in final_df.columns:
                final_df[col] = user_df[col]

        # Predict
        try:
            pred = model.predict(final_df)[0]
        except Exception as e:
            return render_template(
                "index.html",
                result=f"❌ Prediction Error: {str(e)}",
                locations=[]
            )

        price = float(pred)

        # Suggested locations based on predicted budget
        if price < 3000000:
            suggested = POPULAR_LOCATIONS["budget_low"]
        elif price < 8000000:
            suggested = POPULAR_LOCATIONS["budget_mid"]
        else:
            suggested = POPULAR_LOCATIONS["budget_high"]

        return render_template(
            "index.html",
            result=f"Predicted Price: ₹{price:,.2f}",
            locations=suggested
        )
    
    print("Routes:", [rule.rule for rule in app.url_map.iter_rules()])
    return app

if __name__ == "__main__":
    create_app().run(debug=True)