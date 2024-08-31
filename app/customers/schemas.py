from pydantic import BaseModel, Field


class UpdateCustomerRequest(BaseModel):
    id: str = Field(...)
    customer_id: str = Field(...)
    customer_name: str = Field(...)
