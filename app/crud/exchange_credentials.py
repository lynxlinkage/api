from typing import Dict, List, Optional, Union, Any

from sqlalchemy.orm import Session

from app.models.exchange_credential import ExchangeCredentials
from app.schemas.exchange_credentials import ExchangeCredentialsCreate, ExchangeCredentialsUpdate


def get_by_id(db: Session, *, id: int) -> Optional[ExchangeCredentials]:
    """Get exchange credentials by ID"""
    return db.query(ExchangeCredentials).filter(ExchangeCredentials.id == id).first()


def get_by_user_id(db: Session, *, user_id: int) -> List[ExchangeCredentials]:
    """Get all exchange credentials for a specific user"""
    return db.query(ExchangeCredentials).filter(ExchangeCredentials.user_id == user_id).all()


def create(db: Session, *, user_id: int, obj_in: ExchangeCredentialsCreate) -> ExchangeCredentials:
    """Create new exchange credentials for a user"""
    data = obj_in.model_dump()
    db_obj = ExchangeCredentials(user_id=user_id, **data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update(
    db: Session, *, db_obj: ExchangeCredentials, obj_in: Union[ExchangeCredentialsUpdate, Dict[str, Any]]
) -> ExchangeCredentials:
    """Update exchange credentials"""
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True)
    
    for field in update_data:
        setattr(db_obj, field, update_data[field])
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete(db: Session, *, id: int) -> ExchangeCredentials:
    """Delete exchange credentials"""
    obj = db.query(ExchangeCredentials).get(id)
    db.delete(obj)
    db.commit()
    return obj