from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class PaperImport(BaseModel):
    title: str
    abstract: str


class ChatMessage(BaseModel):
    content: str