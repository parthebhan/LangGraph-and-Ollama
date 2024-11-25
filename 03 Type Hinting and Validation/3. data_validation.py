#pip install pydantic[email]
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field, EmailStr

class UserData(TypedDict):
    name: str
    age: int
    email: str

user_data = {"name": "John Doe", "age": 30, "email": "email@example.com"}
data = UserData(user_data)

print("User Data 1:", data)


user_data = {"name": "John Doe", "address": "mumbai"}
data = UserData(user_data)

print("User Data 2:", data)


# using pydantic BaseModel for validation in runtime
class UserModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the user")
    age: int = Field(..., gt=0, description="Age of the user")
    email: EmailStr = Field(..., description="Email of the user")
    sex: Optional[Literal["male", "female", "other"]] = "other"


data = UserModel(name="John Doe", age=30, email="email@example.com")
print("User Data 3:", data)


data = UserModel(name="John Doe", age=30, email="email@example.com", sex="male")
print("User Data 3:", data)