from deta import app

@app.lib.run()
def welcome(event):
    return {
        # access input to your function with event.json
        "message": f"hello {event.json.get('name')}!"
    }

@app.lib.run(action="hello")
def welcome(event):
    return {
        "message": f"hello {event.json.get('name')}!"
    }

@app.lib.run(action="greet")
def greet(event):
    return {
        "message": f"good morning {event.json.get('name')}!"
    }

from datetime import datetime

# CLI run
@app.lib.run()
def say_hello(event):
    return "hello deta"

# CLI run & cron
@app.lib.run(action='time') # action 'time'
@app.lib.cron()
def print_time(event):
    return f"it is {datetime.now()}" 

from deta import App
from fastapi import FastAPI

app = App(FastAPI())

# HTTP
@app.get("/")
def http():
    return "Hello deta, i am running with HTTP"

# CLI run
@app.lib.run()
def run(event):
    return "Hello deta, i am running from the cli"
