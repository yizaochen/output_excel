from typing import List
from datetime import datetime
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import CTBCForeignBankSlip
from transactions.schemas import (
    CreateTransactionRequest,
    UpdateTransactionRequest,
    DeleteTransactionRequest,
    ReadTransactionResponse,
)


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    responses={404: {"description": "API Not found"}},
)
templates = Jinja2Templates(directory="templates")


# CREATE
@router.post("/")
async def create_transaction(
    transaction: CreateTransactionRequest, db: Session = Depends(get_db)
):
    try:
        bank_slip = CTBCForeignBankSlip(
            BankSlipDate=transaction.bank_slip_date,
            CustomerID=transaction.customer_id,
            BankCode=transaction.bank_code,
            BankSlipCurrency=transaction.bank_slip_currency,
            BankSlipAmount=transaction.bank_slip_amount,
            CustomerName=transaction.customer_name,
            BankSlipCustomer=transaction.bank_slip_customer,
            Country=transaction.country,
            FilePath=transaction.file_path,
            PredictType=transaction.predict_type,
            ProcessStatus=transaction.process_status,
            ReferenceNumber=transaction.reference_number,
            RemitType=transaction.remit_type,
            BankSlipRemark=transaction.bank_slip_remark,
            ChangeDate=transaction.change_date,
            ArNo=transaction.ar_no,
        )
        db.add(bank_slip)
        db.commit()
        return JSONResponse(
            content={"message": "Transaction created successfully"},
            status_code=201,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )


# READ
@router.get("/", response_class=HTMLResponse)
async def read_transactions(
    request: Request,
    bank_slip_date_start: str = datetime.now().strftime("%Y-%m-%d"),
    bank_slip_date_end: str = datetime.now().strftime("%Y-%m-%d"),
    bank_slip_customer: str = "All",
    predict_type: str = "All",
    process_status: str = "All",
    reference_number: str = "All",
    db: Session = Depends(get_db),
):
    try:
        start_date = datetime.strptime(bank_slip_date_start, "%Y-%m-%d")
        end_date = datetime.strptime(bank_slip_date_end, "%Y-%m-%d")

        # first criteria:  bank_slip_date_start <=  BankSlipDate <= bank_slip_date_end
        results: List[CTBCForeignBankSlip] = (
            db.query(CTBCForeignBankSlip).filter(
                CTBCForeignBankSlip.BankSlipDate >= start_date,
                CTBCForeignBankSlip.BankSlipDate <= end_date,
            )
        ).all()

        # second criteria:  bank_slip_customer
        if bank_slip_customer != "All":
            results = [
                result
                for result in results
                if result.BankSlipCustomer == bank_slip_customer
            ]

        # third criteria:  predict_type
        if predict_type != "All":
            results = [
                result for result in results if result.PredictType == predict_type
            ]

        # fourth criteria:  process_status
        if process_status != "All":
            results = [
                result for result in results if result.ProcessStatus == process_status
            ]

        # fifth criteria:  reference_number
        if reference_number != "All":
            results = [
                result
                for result in results
                if result.ReferenceNumber == reference_number
            ]

        transactions = [
            ReadTransactionResponse(
                id=result.id,
                bank_slip_date=result.BankSlipDate,
                customer_id=result.CustomerID,
                bank_code=result.BankCode,
                bank_slip_currency=result.BankSlipCurrency,
                bank_slip_amount=result.BankSlipAmount,
                customer_name=result.CustomerName,
                bank_slip_customer=result.BankSlipCustomer,
                country=result.Country,
                file_path=result.FilePath,
                predict_type=result.PredictType,
                process_status=result.ProcessStatus,
                reference_number=result.ReferenceNumber,
                remit_type=result.RemitType,
                bank_slip_remark=result.BankSlipRemark,
                change_date=result.ChangeDate,
                ar_no=result.ArNo,
            )
            for result in results
        ]
        return templates.TemplateResponse(
            "transactions.html", {"request": request, "transactions": transactions}
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )


# UPDATE
@router.put("/")
async def update_transaction(
    transaction: UpdateTransactionRequest, db: Session = Depends(get_db)
):
    try:
        bank_slip = db.query(CTBCForeignBankSlip).filter_by(id=transaction.id).first()
        if not bank_slip:
            return JSONResponse(
                content={"message": "Transaction not found"}, status_code=404
            )
        bank_slip.BankSlipDate = transaction.bank_slip_date
        bank_slip.CustomerID = transaction.customer_id
        bank_slip.BankCode = transaction.bank_code
        bank_slip.BankSlipCurrency = transaction.bank_slip_currency
        bank_slip.BankSlipAmount = transaction.bank_slip_amount
        bank_slip.CustomerName = transaction.customer_name
        bank_slip.BankSlipCustomer = transaction.bank_slip_customer
        bank_slip.Country = transaction.country
        bank_slip.FilePath = transaction.file_path
        bank_slip.PredictType = transaction.predict_type
        bank_slip.ProcessStatus = transaction.process_status
        bank_slip.ReferenceNumber = transaction.reference_number
        bank_slip.RemitType = transaction.remit_type
        bank_slip.BankSlipRemark = transaction.bank_slip_remark
        bank_slip.ChangeDate = transaction.change_date
        bank_slip.ArNo = transaction.ar_no
        db.commit()
        return JSONResponse(
            content={"message": "Transaction updated successfully"},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )


# DELETE
@router.delete("/")
async def delete_transaction(
    transaction: DeleteTransactionRequest, db: Session = Depends(get_db)
):
    try:
        bank_slip = db.query(CTBCForeignBankSlip).filter_by(id=transaction.id).first()
        if not bank_slip:
            return JSONResponse(
                content={"message": "Transaction not found"}, status_code=404
            )
        db.delete(bank_slip)
        db.commit()
        return JSONResponse(
            content={"message": "Transaction deleted successfully"},
            status_code=200,
        )
    except Exception as e:
        return JSONResponse(
            content={"message": f"An error occurred: {e}"}, status_code=500
        )
