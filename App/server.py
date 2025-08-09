from flask import Flask
import json
from .about import me

app = Flask(__name__)#create a Flask application instance

#creating endpoint for the root URL
@app.get("/")
def home():
    return f"Hello world from Flask server!"


@app.get("/test")
def test():
    return f"This is a test endpoint!"

@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)