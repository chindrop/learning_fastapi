import stat
from typing import Optional
from unicodedata import category
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "cotent of post 1", "id": 1}, 
    {"title": "Fatourite food", "content": "Rice liker", "id": 2}]


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/posts", status_code=status.HTTP_201_CREATED )
def create_post(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}

