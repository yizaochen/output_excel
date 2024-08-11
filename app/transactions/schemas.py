from pydantic import BaseModel
import datetime


class CreateTransactionRequest(BaseModel):
    bank_slip_date: datetime.date
    customer_id: str
    bank_code: str
    bank_slip_currency: str
    bank_slip_amount: str
    customer_name: str
    bank_slip_customer: str
    country: str
    file_path: str
    predict_type: str
    process_status: str
    reference_number: str
    remit_type: str
    bank_slip_remark: str
    change_date: datetime.date
    ar_no: str


class UpdateTransactionRequest(BaseModel):
    id: int
    bank_slip_date: datetime.date
    customer_id: str
    bank_code: str
    bank_slip_currency: str
    bank_slip_amount: str
    customer_name: str
    bank_slip_customer: str
    country: str
    file_path: str
    predict_type: str
    process_status: str
    reference_number: str
    remit_type: str
    bank_slip_remark: str
    change_date: datetime.date
    ar_no: str


class DeleteTransactionRequest(BaseModel):
    id: int


class ReadTransactionResponse(BaseModel):
    id: int
    bank_slip_date: datetime.date
    customer_id: str
    bank_code: str
    bank_slip_currency: str
    bank_slip_amount: str
    customer_name: str
    bank_slip_customer: str
    country: str
    file_path: str
    predict_type: str
    process_status: str
    reference_number: str
    remit_type: str
    bank_slip_remark: str
    change_date: datetime.date
    ar_no: str
