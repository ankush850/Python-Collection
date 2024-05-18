from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd

#loading the ML model
with open('model2.pkl','rb') as f:
         model=pickle.load(f)

app=FastAPI()

#pydantic model to validate incoming data
class UserInput(BaseModel):
    site_area:Annotated[int,Field(..., description="site area")]            
    structure_type:Annotated[Literal['Residential','Commercial','Mixed-use','Industrial'],Field(..., description="structure type")]         
    water_consumption:Annotated[float,Field(..., description="water consumption")]        
    recycling_rate:Annotated[int,Field(..., description="recycle rate")]        
    utilisation_rate:Annotated[int,Field(..., description="utilisation rate")]        
    air_qality_index:Annotated[int,Field(..., description="air quality index")]        
    issue_reolution_time:Annotated[int,Field(..., description="issue resolution time")]     
    resident_count:Annotated[int,Field(..., description="resident count")] 

@app.post('/predict')
def predict_electricity_cost(data:UserInput):
      input_df=pd.DataFrame([{
    'site area': data.site_area,         
    'structure type': data.structure_type,       
    'water consumption': data.water_consumption,      
    'recycling rate': data.recycling_rate,       
    'utilisation rate': data.utilisation_rate,     
    'air qality index': data.air_qality_index, 
    'issue reolution time': data.issue_reolution_time,   
    'resident count': data.resident_count 
}])


      prediction=model.predict(input_df)[0]
      return JSONResponse(status_code=200,content={'Predicted_electricty_cost': prediction})



@app.get("/")
def hello():
    return {'message':'Hello World'}