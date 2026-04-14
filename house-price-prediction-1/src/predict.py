@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    Area: float = Form(...),
    Bedrooms: int = Form(...),
    Stories: int = Form(...),
    Parking: int = Form(...),
    Amenities: str = Form("")
):

    print("BACKEND VERSION: NEW")

    amen_list = [a.strip() for a in Amenities.split(",") if a.strip()]
    amen_count = len(amen_list)

    df = pd.DataFrame({
        "Area": [Area],
        "Bedrooms": [Bedrooms],
        "Bathrooms": [1],
        "Stories": [Stories],
        "Parking": [Parking],
        "amen_count": [amen_count],
        "city_num": [0]
    })

    try:
        # 🔥 Absolute-force fix: match EXACT model columns and fill everything else with 0
        model_columns = list(model.feature_names_in_)
        final_df = pd.DataFrame(0, index=[0], columns=model_columns)

        # Fill ONLY matching columns
        for col in df.columns:
            if col in final_df.columns:
                final_df[col] = df[col]

        pred = model.predict(final_df)[0]

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "result": f"Error during prediction: {e}",
                "locations": []
            }
        )

    price = float(pred)

    if price < 3000000:
        suggested = ["Tambaram", "Avadi", "Perambur"]
    elif price < 8000000:
        suggested = ["Velachery", "Anna Nagar", "Madipakkam"]
    else:
        suggested = ["Adyar", "Besant Nagar", "ECR"]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": f"Predicted Price: ₹{price:,.2f}",
            "locations": suggested,
        }
    )
