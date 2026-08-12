from fastapi import APIRouter, Depends

from schemas import *
from db import get_db
import service
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/checkout")
def save_to_database(checkout: CheckoutScheme, session: Session = Depends(get_db))
    return service.process_checkout(checkout, session)
