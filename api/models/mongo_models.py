from pydantic import BaseModel, Field
from typing import Optional

class Data(BaseModel):
    name: str = Field(..., # ... means required
                      example="John Doe",
                      description="Your name")
    description: Optional[str] = Field(None,
                                       example="A description of you",
                                       description="A description of you")
    age: Optional[int] = Field(None,
                               example=42,
                               description="Your age")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "age": self.age
        }

class DataInDB(Data):
    id: str = Field(...,
                    example="507f1f77bcf86cd799439011",
                    description="The unique identifier of the data")
    created: str = Field(...,
                         example="2020-01-01T00:00:00.000Z",
                         description="The date and time the data was created")
    modified: str = Field(...,
                          example="2020-01-01T00:00:00.000Z",
                          description="The date and time the data was last modified")

class UpdateData(BaseModel):
    name: Optional[str] = Field(None,
                                example="John Doe",
                                description="Your name")
    description: Optional[str] = Field(None,
                                       example="A description of you",
                                       description="A description of you")
    age: Optional[int] = Field(None,
                               example=42,
                               description="Your age")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "age": self.age
        }