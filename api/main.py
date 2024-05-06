from fastapi import FastAPI

from api.models.post import UserPost, UserPostIn

app = FastAPI()


# prelim implementation is a dictionary
post_table = {}


# because the post is a pydantic model, the json input will automatically
# be converted into the UserPostIn object
@app.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@app.get("/post", response_model=list[UserPost])
async def list_posts():
    return list(post_table.values())


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
