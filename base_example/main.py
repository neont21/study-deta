from fastapi import FastAPI
from .routers import users

tags_metadata = [
    {
        'name': 'users',
        'description': 'Operations with users',
    }
]

app = FastAPI(
    title='DETA Base Test',
    description='Deta Base test with FastAPI',
    openapi_tags=tags_metadata)

app.include_router(users.router)
