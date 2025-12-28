# Serving the ML model as an API using FastAPI

# A quick start:
```text
Here, we've first developed a ML model and saved it using pickle, and then we've used FastAPI with Pydantic to serve it as an API.
```

# Stacks used:
- Python
- FastAPI
- Pandas
- sklearn
- pickle


- Create a virtual Environment, activate it and then run the following command:-
```bash
pip install -r requirements.txt
```

- command to run the API:-
```terminal
uvicorn app:app --reload
```
``` Text
Go to the url/docs for making predictions
```