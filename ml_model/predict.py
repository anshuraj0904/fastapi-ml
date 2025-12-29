import pickle
import pandas as pd


# Opening the ml model
with open("./ml_model/model.pkl","rb") as f:
    model = pickle.load(f)



# Enhancing the prediction:-
class_labels = model.classes_.tolist() # randomforest has the classes and their respective probabilities.


# This(MODEL_VERSION) generally comes via MLFlow registry.
MODEL_VERSION = "1.0.7" # This is for deployments. 


def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])

    predicted_class = model.predict(input_df)[0]


    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    class_probabilities = dict(zip(class_labels, probabilities)) 

    return {
        "predicted category":predicted_class,
        "confidence":round(confidence,4),
        "class_probabilities":class_probabilities
    }