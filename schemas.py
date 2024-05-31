from pydantic import BaseModel, Field

class RegisterModel(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class LoginModel(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True