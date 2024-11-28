from pydantic import BaseModel, Field


class Filter(BaseModel):
    # Not Null
    location: str = Field(max_length=50, min_length=3)
    price: float = Field(default=1000, ge=20, le=10000)
    room: int = Field(default=1, ge=1, le=10)
