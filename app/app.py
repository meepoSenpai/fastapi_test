
import uvicorn
import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from .routes.user import router as user_router
from .routes.auth import router as auth_router
from .routes.todo import router as todo_router

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(todo_router)