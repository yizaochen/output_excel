from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import CTBCForeignSAP
from customers.schemas import UpdateCustomerRequest


router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={404: {"description": "API Not found"}},
)
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "customers.html",
        {
            "request": request,
            "active_page": "Customers",
        },
    )


@router.get("/search-by-name", response_class=HTMLResponse)
async def search_by_name(
    request: Request,
    customerName: str = None,
    db: Session = Depends(get_db),
):
    if customerName:
        customers = (
            db.query(CTBCForeignSAP)
            .filter(CTBCForeignSAP.CustomerName.like(f"%{customerName}%"))
            .all()
        )
    else:
        customers = db.query(CTBCForeignSAP).all()
    return templates.TemplateResponse(
        "customers_table.html",
        {
            "request": request,
            "active_page": "Customers",
            "customers": customers,
        },
    )


@router.get("/search-by-id", response_class=HTMLResponse)
async def search_by_id(
    request: Request,
    customerID: str = None,
    db: Session = Depends(get_db),
):
    if customerID:
        customers = (
            db.query(CTBCForeignSAP)
            .filter(CTBCForeignSAP.CustomerID.like(f"%{customerID}%"))
            .all()
        )
    else:
        customers = db.query(CTBCForeignSAP).all()
    return templates.TemplateResponse(
        "customers_table.html",
        {
            "request": request,
            "active_page": "Customers",
            "customers": customers,
        },
    )


@router.get("/show-all", response_class=HTMLResponse)
async def show_all(request: Request, db: Session = Depends(get_db)):
    customers = db.query(CTBCForeignSAP).all()
    return templates.TemplateResponse(
        "customers_table.html",
        {
            "request": request,
            "active_page": "Customers",
            "customers": customers,
        },
    )


# UPDATE
@router.post("/update")
async def update_transaction(
    customer_request: UpdateCustomerRequest,
    db: Session = Depends(get_db),
):
    try:
        customer = db.query(CTBCForeignSAP).filter_by(id=customer_request.id).first()
        if not customer:
            return JSONResponse(
                content={"message": "Customer not found"}, status_code=404
            )
        customer.CustomerID = customer_request.customer_id
        customer.CustomerName = customer_request.customer_name
        db.commit()
        return JSONResponse(
            content={"message": "Customer updated successfully"},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )
