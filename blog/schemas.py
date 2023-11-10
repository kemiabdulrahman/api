from pydantic import BaseModel

# Base Model 
class Blog(BaseModel):
    title: str
    body: str

