#pip install pydantic[email]
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field, EmailStr


# Using TypedDict for defining a dictionary with a specific structure
# no run time validation check
class UserData(TypedDict):
    name: str
    age: int
    email: str

# 1
user_data = {"name": "KGP Talkie", "age": 30, "email": "udemy@kgptalkie.com"}
data = UserData(user_data)
print("User data:", data)

# 2
user_data = {"names": "KGP Talkie"}
data = UserData(user_data)
print("User data:", data)

# Using Pydantic for data validation
class UserModel(BaseModel):
    name: str = Field(..., min_length=1, description="User's full name (non-empty)")
    age: int = Field(..., gt=0, description="User's age (must be > 0)")
    email: EmailStr = Field(..., description="User's email address (valid email format)")
    sex: Optional[Literal["male", "female", "other"]] = "other"


user_data = UserModel(name="KGP Talkie", age=35, email="example@email.com")
print("Pydantic validation passed 1:", user_data)

user_data = {"name": "KGP Talkie", "age": 30, "email": "udemy@kgptalkie.com"}
user = UserModel(**user_data)
print("Pydantic validation passed 2:", user)

# Pydantic example with invalid data
# UserModel(name="KGP Talkie", age=-5, email="example@email.com")


