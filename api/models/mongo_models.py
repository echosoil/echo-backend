from pydantic import BaseModel, Field
from typing import Optional, List


class File(BaseModel):
    bucket: str = Field(..., example="my_bucket", description="The bucket name")
    file: str = Field(..., example="my_file.txt", description="The object name")
    
    def to_dict(self):
        return {
            "bucket": self.bucket,
            "file": self.file
        }


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
    files: Optional[List[File]] = Field(None, description="List of files")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "age": self.age,
            "files": [file.model_dump() for file in self.files] if self.files else None
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
    files: Optional[List[File]] = Field(None, description="List of files")

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "age": self.age,
            "files": [file.model_dump() for file in self.files] if self.files else None
        }
