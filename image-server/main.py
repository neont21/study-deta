from fastapi import FastAPI
from .routers import images

tags_metadata = [
    {
        'name': 'images',
        'description': 'Upload/Download the images',
    }
]

app = FastAPI(
    title='DETA Drive Test',
    description='Deta Drive test with FastAPI',
    openapi_tags=tags_metadata)

app.include_router(images.router)
