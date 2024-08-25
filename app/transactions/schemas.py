from pydantic import BaseModel, Field
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
    id: str = Field(...)
    bank_slip_date: str = Field(...)
    customer_id: str = Field(...)
    bank_code: str = Field(...)
    bank_slip_currency: str = Field(...)
    bank_slip_amount: str = Field(...)
    customer_name: str = Field(...)
    bank_slip_customer: str = Field(...)
    country: str = Field(...)
    file_path: str = Field(...)
    predict_type: str = Field(...)
    process_status: str = Field(...)
    reference_number: str = Field(...)
    remit_type: str = Field(...)
    bank_slip_remark: str = Field(...)
    change_date: str = Field(...)
    ar_no: str = Field(...)


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
