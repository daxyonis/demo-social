# Models are for data validation
# This is the model for data input (= like the DTO for input)
from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str


# This is the model for db
class UserPost(UserPostIn):
    id: int
