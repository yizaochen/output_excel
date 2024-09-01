from pydantic import BaseModel, Field


class UpdateCustomerRequest(BaseModel):
    id: str = Field(...)
    customer_name: str = Field(...)


class AddCustomerRequest(BaseModel):
    customer_name: str = Field(...)


class DeleteCustomerRequest(BaseModel):
    id: str = Field(...)
