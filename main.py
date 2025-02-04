from fastapi import FastAPI
import pandas as pd

# creats API object
app = FastAPI()

# road data
data = pd.read_csv('data.csv')

#coba root home API (get)
@app.get("/")
def root():
    return {'message' : 'My first API !'}

#endpoint sapaan

@app.get("/name/{name}")
def greet (name):
    return {'message' : f'Hai {name}, how are you ?'}

#endpoint return data
@app.get("/data")
def get_data():
    return data.to_dict(orient='records')

@app.get("/data/{id}")
def search_data(id:int):
    result = data[data['id']==id]
    return {'result':result.to_dict(orients='records')}

