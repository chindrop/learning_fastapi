from typing import Optional
from unicodedata import category
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    category: list
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "cotent of post 1", "id": 1}, {"title": "Fatourite food", "content": "Rice liker", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_user():
    return {"data": my_posts}


@app.post("/posts",)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}