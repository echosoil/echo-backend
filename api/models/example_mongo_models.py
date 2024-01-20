from pydantic import BaseModel, Field
from typing import Optional

class Data(BaseModel):
    name: str = Field(..., # ... means required
                      example="John Doe",
                      description="Your name")
    age: Optional[int] = Field(None,
                               example=42,
                               description="Your age")

class DataInDB(Data):
    id: str = Field(...,
                    example="507f1f77bcf86cd799439011",
                    description="The unique identifier of the data")

class UpdateData(BaseModel):
    name: Optional[str] = Field(None,
                                example="John Doe",
                                description="Your name")
    age: Optional[int] = Field(None,
                               example=42,
                               description="Your age")
