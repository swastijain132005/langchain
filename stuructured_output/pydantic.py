from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class student(BaseModel):
    name: str
    age: int
    grade: str


new_student = student(name="Alice", age=20, grade="A")

student=student(**new_student)

print(student)

# default values

class student(BaseModel):
    name: str = "Bob"
    age: int = 76
    grade: str = "C"

new_student = {}

student=student(**new_student)

print(student)

class student(BaseModel):
    name: str = "Bob"
    #if not given use default value
    age: Optional[int] = None
    email:EmailStr #checks if the email is valid
    cgpa: float = Field(gt=0, lt=4.0,default=5,description='a decimal value represent cgPA') #checks if the cgpa is between 0 and 4.0


new_student = {}

student=student(**new_student)

student_dict=dict(student)

print(student_dict['age'])