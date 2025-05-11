from typing import Dict, Optional, Any
from pydantic import BaseModel, Field


class ExchangeCredentialsBase(BaseModel):
    exchange_name: str
    api_key: Optional[str] = None
    auth_params: Dict[str, Any] = Field(default_factory=dict)
    description: Optional[str] = None
    is_active: bool = True


class ExchangeCredentialsCreate(ExchangeCredentialsBase):
    pass


class ExchangeCredentialsUpdate(ExchangeCredentialsBase):
    exchange_name: Optional[str] = None


class ExchangeCredentialsInDBBase(ExchangeCredentialsBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class ExchangeCredentials(ExchangeCredentialsInDBBase):
    pass