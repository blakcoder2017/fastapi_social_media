# from pydantic import BaseModel, ConfigDict, EmailStr, Field
# from pydantic.types import conint
# from datetime import datetime
# from typing import Annotated

# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str

# #response schema
# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime
    
#     model_config = ConfigDict(from_attributes=True)

# #User login schema 
# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str


# class PostBase(BaseModel):
#     title: str
#     content: str
#     published: bool | None = True
    
# class PostCreate(PostBase):
#     pass

# #response schema
# class Post(PostBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     owner: 'UserOut'
    
    
#     model_config = ConfigDict(from_attributes=True)
    
# class PostOut(BaseModel):
#     Post: Post
#     votes: int

    
# # Token schema
# class Token(BaseModel):
#     access_token: str
#     token_type: str

# # Token Data schema
# class TokenData(BaseModel):
#     id: int | None = None
    

# class Vote(BaseModel):
#     post_id: int
#     dir: Annotated[int, Field(ge=0, le=1)]  # dir can only be 0 or 1
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime
from typing import Annotated, Optional

# =======================
# User Schemas
# =======================
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# =======================
# Post Schemas
# =======================
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: Optional[UserOut]  # optional helps prevent null owner issues

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = ConfigDict(from_attributes=True)


# =======================
# Token Schemas
# =======================
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


# =======================
# Vote Schema
# =======================
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]  # dir can only be 0 or 1
