from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from transactions.routes import router as transactions_router
from core.models import Base
from core.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(transactions_router)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    bank_slip_date_start = datetime.now().strftime("%Y-%m-%d")
    bank_slip_date_end = datetime.now().strftime("%Y-%m-%d")
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "bank_slip_date_start": bank_slip_date_start,
            "bank_slip_date_end": bank_slip_date_end,
        },
    )
