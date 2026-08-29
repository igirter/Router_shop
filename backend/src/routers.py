from fastapi import APIRouter, Depends

from src.schemas import *
from src.db import get_db
import src.service
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/checkout")
def save_to_database(checkout: CheckoutScheme, session: Session = Depends(get_db)):
    return service.process_checkout(checkout, session)
