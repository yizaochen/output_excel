from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from transactions.routes import router as transactions_router
from customers.routes import router as customers_router
from d_customers.routes import router as d_customers_router
from core.models import Base
from core.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(transactions_router)
app.include_router(customers_router)
app.include_router(d_customers_router)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # bank_slip_date_start = datetime.now().strftime("%Y-%m-%d")
    bank_slip_date_start = "2019-01-01"
    bank_slip_date_end = datetime.now().strftime("%Y-%m-%d")
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "active_page": "Transactions",
            "bank_slip_date_start": bank_slip_date_start,
            "bank_slip_date_end": bank_slip_date_end,
        },
    )
