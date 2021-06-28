from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
PROJECT_KEY = os.getenv('PROJECT_KEY')
DRIVE_NAME = os.getenv('DRIVE_NAME')

deta = Deta(PROJECT_KEY)
drive = deta.Drive(DRIVE_NAME)

router = APIRouter(tags=['images'])

@router.get('/', response_class=HTMLResponse)
def render():
    return '''
        <form action='/upload'enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <input type="submit">
        </form>
    '''

@router.post('/upload')
def upload_image(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    result = drive.put(name, f)
    return result

@router.get('/download/{name}', response_class=StreamingResponse)
def download_image(name: str):
    result = drive.get(name)
    return StreamingResponse(result.iter_chunks(1024), media_type='image/png')
