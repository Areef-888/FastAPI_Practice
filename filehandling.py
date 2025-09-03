from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional,List

class User(BaseModel):
    name:str
    id:int


#name="Areef"

data={
    'name':'areef',
    'id':123
}
user_name=User(**data)    
print(user_name)
#---------------------------------------------------------------------------------------------------
class Food(BaseModel):
    name:str
    price:Optional[int]=None
    Incredients:Optional[List[str]]=None

class restaurent(BaseModel):
    name:str=Field(..., pattern=r'[A-Z a-z]+')
    location:str
    email:EmailStr
    food:List[Food]   



data1={
    "name":"123Big B",
    "location":'Banglore',
    "email":"bigb@gmail.com",
    "food":[
        {'name':'Berger','price':1234,'Incredients':['X','Y','Z']},
        {'name':'Pizza'}
    ]
}
restaurent_instance=restaurent(**data1)

print(restaurent_instance)


#------------------------------------------------------------------------------------------


class car(BaseModel):
    name:str


    @field_validator("name")
    @classmethod

    def name_contains_space(cls,v:str):
        if " " in v:
            raise ValueError("Name contains space")
        return v
    
c=car(name="CRETA")    
print(c)


#-----------------------------------------------------------------------------------------------------------

