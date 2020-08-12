from pydantic import BaseModel
from typing import Optional


class Shortener(BaseModel):
    url: str
    expiry_time: Optional[int] = 60

