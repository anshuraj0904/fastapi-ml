# Serving the ML model as an API using FastAPI

# A quick start:
```text
Here, we've first developed a ML model and saved it using pickle, and then we've used FastAPI with Pydantic to serve it as an API.
Next up, we've created a minimal usage frontend using streamlit to test the api endpoint.
```

# Stacks used:
- Python
- FastAPI
- Pandas
- sklearn
- pickle
- streamlit
- uvicorn
- requests


- Create a virtual Environment, activate it and then run the following command:-
```bash
pip install -r requirements.txt
```

- command to run the Application:-
- 1. The Backend
```bash
uvicorn app:app --reload
```
- 2. The Frontend
``` bash 
streamlit run frontend.py
```
