from fastapi import FastAPI

app = FastAPI(
    title='DETA Micros Test',
    description='Deta Micros test with FastAPI')

@app.get('/')
def hello_world():
    return 'Hello World'
