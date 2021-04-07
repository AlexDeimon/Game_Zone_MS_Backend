from pydantic import BaseModel
class AdminIn(BaseModel):
    username: str
    password: str
class AdminOut(BaseModel):
    username: str