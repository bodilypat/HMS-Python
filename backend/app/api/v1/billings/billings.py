#app/api/v1/billings/billing.py

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.billing import Billing
from app.schemas.billings.billing import BillingCreate, BillingUpdate
from app.api.v1.billings.billing import (
    create_billing as _create_billing,
    get_billings as _get_billings,
    get_billings as _get_billing,
    update_billing as _update_billing,
    delete_billing as _delete_billing,
)

#--------------------------------
# CREATE 
#--------------------------------
def create_billing(
        db: Session, 
        billing: BillingCreate
        ) -> Billing:
    return _create_billing(db=db, billing=billing)

#--------------------------------
# READ 
#--------------------------------
def get_billings(
        db: Session, 
        skip: int = 0, 
        limit: int = 100
        ) -> List[Billing]:
    return _get_billings(db=db, skip=skip, limit=limit)

#--------------------------------
# READ BY ID
#--------------------------------
def get_billing(
        db: Session, 
        billing_id: int
        ) -> Optional[Billing]:
    return _get_billing(db=db, billing_id=billing_id)

#--------------------------------
# UPDATE
#--------------------------------
def update_billing(
        db: Session, 
        billing_id: int, 
        billing: BillingUpdate
        ) -> Optional[Billing]:
    return _update_billing(db=db, billing_id=billing_id, billing=billing)

#--------------------------------
# DELETE
#--------------------------------
def delete_billing(
        db: Session, 
        billing_id: int
        ) -> Optional[Billing]:
    return _delete_billing(db=db, billing_id=billing_id)




