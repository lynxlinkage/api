from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_active_user, get_db
from app.models.user import User
from app.schemas.exchange_credentials import ExchangeCredentials, ExchangeCredentialsCreate, ExchangeCredentialsUpdate

router = APIRouter()


@router.get("/", response_model=List[ExchangeCredentials])
def read_exchange_credentials(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get all exchange credentials for current user.
    """
    credentials = crud.exchange_credentials.get_by_user_id(db, user_id=current_user.id)
    return credentials


@router.post("/", response_model=ExchangeCredentials)
def create_exchange_credentials(
    *,
    db: Session = Depends(get_db),
    credentials_in: ExchangeCredentialsCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create new exchange credentials.
    """
    credentials = crud.exchange_credentials.create(db, user_id=current_user.id, obj_in=credentials_in)
    return credentials


@router.put("/{credentials_id}", response_model=ExchangeCredentials)
def update_exchange_credentials(
    *,
    db: Session = Depends(get_db),
    credentials_id: int,
    credentials_in: ExchangeCredentialsUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update exchange credentials.
    """
    credentials = crud.exchange_credentials.get_by_id(db, id=credentials_id)
    if not credentials or credentials.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Exchange credentials not found")
    
    credentials = crud.exchange_credentials.update(db, db_obj=credentials, obj_in=credentials_in)
    return credentials


@router.delete("/{credentials_id}", response_model=ExchangeCredentials)
def delete_exchange_credentials(
    *,
    db: Session = Depends(get_db),
    credentials_id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Delete exchange credentials.
    """
    credentials = crud.exchange_credentials.get_by_id(db, id=credentials_id)
    if not credentials or credentials.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Exchange credentials not found")
    
    credentials = crud.exchange_credentials.delete(db, id=credentials_id)
    return credentials