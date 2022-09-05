from fastapi import APIRouter, Response, status
from config.db import client
from schemas.users import userEntity, usersEntity
from models.users import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

users = APIRouter()


@users.get('/users', response_model=list[User], tags=["users"])
def get_users():
    return usersEntity(client.anchor.users.find())


@users.post('/users', response_model=User, tags=["users"])
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = client.anchor.users.insert_one(new_user).inserted_id
    return userEntity(client.anchor.users.find_one({"_id": id}))


@users.get('/users/{id}', response_model=User, tags=["users"])
def get_user(id: str):
    user = client.anchor.users.find_one({"_id": ObjectId(id)})
    return userEntity(user)


@users.put('/users/{id}', response_model=User, tags=["users"])
def update_user(id: str, user: User):
    client.anchor.users.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(client.anchor.users.find_one({"_id": ObjectId(id)}))


@users.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def get_user(id: str):
    client.anchor.users.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
