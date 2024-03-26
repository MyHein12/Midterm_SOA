from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2
from pathlib import Path




app = FastAPI()

# Sử dụng StaticFiles để phục vụ các tệp CSS và JavaScript
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute()/"static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"name":"hello"})