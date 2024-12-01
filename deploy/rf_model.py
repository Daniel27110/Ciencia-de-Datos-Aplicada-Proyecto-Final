from joblib import load

class PredictionModel_rf:

    def __init__(self):
        self.model = load("rf_model.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
