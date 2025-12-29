# Now that we're done with training the data and creating pickle files. We'll now work on using it in our api. 
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse 
from schema.user_model import UserInput  
from ml_model.predict import model, predict_output
# Creating an instance of the FastAPI.
app = FastAPI()
  


# @app.get("/")
# def home():
#     return JSONResponse(status_code=200, content={"message":"Welcome to the prediction API, go to /predict or /docs for making predictions"})

# Now, the main thing and thet is the route:
@app.post("/predict")
def predict_premium(user_data:UserInput):
    # We'll have to convert the user input to a pandas dataframe.
    user_input = {
         "bmi":user_data.bmi,
         "age_group":user_data.age_group,
         "lifestyle_risk":user_data.lifestyle_risk,
         "city_tier":user_data.city_tier,
         "income_lpa":user_data.income_lpa,
         "occupation":user_data.occupation
    }


    # Putting the response in a try-except block:
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content={"insurance_premium_category":prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)})