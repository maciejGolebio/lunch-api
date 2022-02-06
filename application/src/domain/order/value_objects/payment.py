from typing import Optional
from pydantic import BaseModel, validator


class Payment(BaseModel):
    """"
        Payment in the context of order is only information about the payment method.
    """
    blik: Optional[str] = None
    bank_account: Optional[str] = None

    @validator('blik', always=True)
    def check_blik_or_bank_account(cls, value, values):
        if 'bank_account' not in values and not value:
            raise ValueError('either bank account or blik is required')
        return value
