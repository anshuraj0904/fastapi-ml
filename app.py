# Now that we're done with training the data and creating pickle files. We'll now work on using it in our api. 
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse 
from pydantic import BaseModel,Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd



# Opening the ml model
with open("model.pkl","rb") as f:
    model = pickle.load(f)     

# Creating an instance of the FastAPI.
app = FastAPI()


# List of tier_1 and tier_2 cities:
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]



class UserInput(BaseModel):
    age:Annotated[int,
                  Field(..., gt=0, lt=120, description="Age of the person")
                  ]
    weight: Annotated[float,
                      Field(..., gt=0, description="Weight of the person in Kgs", strict=True)
                      ]
    height: Annotated[float,
                      Field(..., gt=1, description="Height of the person in meters", strict=True)
                      ]
    income_lpa: Annotated[float,
                          Field(...,description="Income of the person in LPA", strict=True)
                          ]
    smoker: Annotated[bool,
                      Field(..., description="Whether the person is a smoker or not",strict=True)
                      ]
    city: Annotated[str,
        Field(..., description="City of the person")
        ]
    occupation: Annotated[str,
                          Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job']
       ,Field(..., description="Occupation of the person", examples=["retired", "unemployed",])
       ]


    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi >30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        

    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
          return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3
    


# @app.get("/")
# def home():
#     return JSONResponse(status_code=200, content={"message":"Welcome to the prediction API, go to /predict or /docs for making predictions"})

# Now, the main thing and thet is the route:
@app.post("/predict")
def predict_premium(user_data:UserInput):
    # We'll have to convert the user input to a pandas dataframe.
    input_df = pd.DataFrame([{
         "bmi":user_data.bmi,
         "age_group":user_data.age_group,
         "lifestyle_risk":user_data.lifestyle_risk,
         "city_tier":user_data.city_tier,
         "income_lpa":user_data.income_lpa,
         "occupation":user_data.occupation
    }])

    prediction = model.predict(input_df)
    # Since the paramters and the pipeline of the model were dumped together, so the pipeline automatically gets implemented. 
    print(prediction)

    return JSONResponse(content={"insurance_premium_category":prediction[0]})