from fastapi import FastAPI
from routes.users import users

app = FastAPI(
    title="REST API using FastAPI and MongoDB",
    description="Simple REST API with FastAPI and MongoDB",
    version="0.1"
)

app.include_router(users)