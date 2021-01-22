"""Faster Payments Transaction Schemas."""
from enum import Enum
from typing import NewType, Optional

from monzo_webhook.model import Model
from monzo_webhook.types import BeneficiaryAccountType, EntrySetID, UserID

FPID = NewType("FPID", str)


class FasterPaymentsCounterParty(Model):

    account_number: str
    sort_code: str
    name: str
    beneficiary_account_type: Optional[BeneficiaryAccountType]
    user_id: UserID


class FPInitiator(Enum):

    CUSTOMER = "customer"


class FPTransactionMetadata(Model):

    action_code: Optional[str]
    confirmation_of_payee_decision_id: Optional[str]
    confirmation_of_payee_requester_id: Optional[UserID]
    faster_payment: bool
    faster_payment_initiator: Optional[FPInitiator]
    fps_fpid: FPID
    fps_payment_id: FPID
    insertion: EntrySetID
    notes: str
    outbound_payment_trace_id: Optional[str]
    trn: str
