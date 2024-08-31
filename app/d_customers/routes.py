from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import CTBCForeignSpecialCustomer
from d_customers.schemas import UpdateCustomerRequest


router = APIRouter(
    prefix="/d_customers",
    tags=["d_customers"],
    responses={404: {"description": "API Not found"}},
)
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db)):
    customers = db.query(CTBCForeignSpecialCustomer).all()

    return templates.TemplateResponse(
        "d_customers.html",
        {
            "request": request,
            "active_page": "D-type-Customers",
            "customers": customers,
        },
    )


@router.post("/add")
async def add_transaction(
    new_customer_name: str,
    db: Session = Depends(get_db),
):
    try:
        new_customer = CTBCForeignSpecialCustomer(CustomerName=new_customer_name)
        db.add(new_customer)
        db.commit()

        # get the id of the newly added customer
        new_customer_id = new_customer.id

        return JSONResponse(
            content={
                "message": "D-type Customer added successfully",
                "id": new_customer_id,
                "name": new_customer_name,
            },
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )


@router.post("/delete")
async def delete_transaction(
    customer_id: int,
    db: Session = Depends(get_db),
):
    try:
        customer = (
            db.query(CTBCForeignSpecialCustomer).filter_by(id=customer_id).first()
        )
        if not customer:
            return JSONResponse(
                content={"message": "D-type Customer not found"}, status_code=404
            )
        db.delete(customer)
        db.commit()
        return JSONResponse(
            content={"message": "D-type Customer deleted successfully"},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )


@router.post("/update")
async def update_transaction(
    customer_request: UpdateCustomerRequest,
    db: Session = Depends(get_db),
):
    try:
        customer = (
            db.query(CTBCForeignSpecialCustomer)
            .filter_by(id=customer_request.id)
            .first()
        )
        if not customer:
            return JSONResponse(
                content={"message": "D-type Customer not found"}, status_code=404
            )
        customer.CustomerName = customer_request.customer_name
        db.commit()
        return JSONResponse(
            content={"message": "D-type Customer updated successfully"},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )
