from pydantic import BaseModel, validator, conint
import datetime
from enum import Enum
from typing import Optional

class Level(Enum):
    BEGINNER = 1,
    INTERMEDIATE = 2,
    ADVANCED = 3




class Programmer(BaseModel):
    first_name: str
    last_name: str
    age: int
    date_employed: datetime.date
    level: Optional[Level]


    @validator("age")
    def validate_age(cls, age):
        if age < 10:
            raise ValueError("age has to be greater than 13")
        return age


    @validator("level")
    def validate_level(cls, level, values):
        if level is not None:
            if level is level.ADVANCED and values['age'] <= 14:
                raise ValueError("To be in advanced level, age must be greater than 14")
        return level





prog_1 = Programmer(
        first_name='Enny',
        last_name='joe', 
        age=18, 
        date_employed=datetime.date(2023, 3, 2), level=Level.ADVANCED)

prog_2 = Programmer(
        first_name='James',
        last_name='Joseph', 
        age=17, 
        date_employed=datetime.date(2023, 3, 2), level=Level.ADVANCED)


print(prog_1)
print(prog_2.json())

