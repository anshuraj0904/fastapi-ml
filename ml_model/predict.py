
import pickle
import pandas as pd



# Opening the ml model
with open("./ml_model/model.pkl","rb") as f:
    model = pickle.load(f)   


def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)
    # Since the paramters and the pipeline of the model were dumped together, so the pipeline automatically gets implemented. 

    print(prediction)

    return prediction[0]