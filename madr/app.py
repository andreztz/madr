from http import HTTPStatus

from fastapi import FastAPI

from madr.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def root():
    return {"message": "Hello, world!"}
