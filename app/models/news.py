from pydantic import BaseModel

class News(BaseModel):
    id: int
    slug: str
    title: str
    content: str
    tag: list