from pydantic import BaseModel

class News(BaseModel):
    id: int
    slug: str | None
    title: str
    content: str
    tag: list