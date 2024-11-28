from pydantic import BaseModel


response_format = (
    "[{\"name\":\"Craigslist SF\","
    "\"description\":\"Craigslist is a popular platform for finding cheaper, "
    "no-fee rentals, including apartments under {amount}.\","
    "\"link\":\"craigslist.org/sfbay\","
    "\"price\":\"Under 1500$\","
    "\"other\":\"Be sure to check regularly, as listings can change "
    "frequently.\"}]"
)


class House(BaseModel):
    name: str
    description: str
    link: str
    price: str
    other: str


class HouseOutput(BaseModel):
    steps: list[House]
