from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Annotated, Union
from fastapi import FastAPI, Form, Request, Header
from backbone import get_result

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#result = "One"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/result1")
async def result1(request: Request):
    form = await request.form()
    result_value = get_result(form)
    return templates.TemplateResponse(
        request=request, name="result1.html", context={"result1": result_value}
    )

# to test
# uvicorn app:app --reload --port 7000