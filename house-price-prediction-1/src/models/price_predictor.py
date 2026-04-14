class PricePredictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        self.load_model()

    def load_model(self):
        import joblib
        self.model = joblib.load(self.model_path)

    def predict_price(self, features):
        if self.model is None:
            raise Exception("Model not loaded.")
        return self.model.predict([features])[0]