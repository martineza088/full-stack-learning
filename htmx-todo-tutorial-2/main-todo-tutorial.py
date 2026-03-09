# FastAPI imports
from fastapi import FastAPI, Request, Header, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.encoders import jsonable_encoders # converts objects to JSON compatible formats

# Other imports
from uuid import uuid4 # makes it possible to create unique IDs for each todo list task
from typing import Annotated, Union

# Initializing FastAPI
app = FastAPI() # instantiates fastapi and creates the app object

# configuring templates directory for Jinja2
templates = Jinja2Templates(directory = "templates")

