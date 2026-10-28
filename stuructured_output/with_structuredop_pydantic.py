from lanchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
from pydantic import BaseModel,Optional ,Field

load_dotenv()

model=ChatOpenAI()

class Review(TypedDict):
    summary:str=Field(description="A brief summary of the review")
    pros:Optional[list[str]]=Field(default='None',description="Write down all the pros inside a list")
    cons:Optional[list[str]]=Field(default=None,description="write down all the cons inside a list")

structured_model=model.with_structured_output(Review)


result=structured_model.invoke("")