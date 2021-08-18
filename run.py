from flask import Flask
from models.db_model import db
from app import app
from routes.endpoints import *


if __name__ == "__main__":
    app.run(debug=True)
    