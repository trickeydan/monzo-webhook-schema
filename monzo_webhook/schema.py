"""Monzo Webhook Schema."""
from datetime import datetime
from enum import Enum
from typing import Any, Dict, NewType, Optional, Union

from pydantic import BaseModel

TabID = NewType("TabID", str)
Category = NewType("Category", str)
AccountID = NewType("AccountID", str)
DeDupeID = NewType("DeDupeID", str)
UserID = NewType("UserID", str)
TransactionID = NewType("TransactionID", str)
P2PTransferID = NewType("P2PTransferID", str)

FPID = NewType("FPID", str)
EntrySetID = NewType("EntrySetID", str)


class Currency(Enum):

    GBP = "GBP"


class P2PInitiator(Enum):

    TAB = "tab"


class BeneficiaryAccountType(Enum):

    PERSONAL = "Personal"


class TransactionScheme(Enum):

    P2P = "p2p_payment"
    FASTER_PAYMENTS = "payport_faster_payments"


class P2PTransactionCounterparty(BaseModel):

    class Config:
        extra = "forbid"

    account_id: AccountID
    name: str
    preferred_name: str
    user_id: UserID


class P2PTransactionMetadata(BaseModel):

    class Config:
        extra = "forbid"

    p2p_initiator: P2PInitiator
    p2p_transfer_id: P2PTransferID
    tab_id: TabID


class FasterPaymentsCounterParty(BaseModel):

    class Config:
        extra = "forbid"

    account_number: str
    sort_code: str
    name: str
    beneficiary_account_type: Optional[BeneficiaryAccountType]
    user_id: UserID


class FPInitiator(Enum):

    CUSTOMER = "customer"


class FPTransactionMetadata(BaseModel):

    class Config:
        extra = "forbid"

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


class TransactionCreatedData(BaseModel):

    class Config:
        extra = "forbid"

    id: TransactionID
    created: datetime
    description: str
    amount: int
    currency: Currency
    notes: str
    category: Category
    categories: Optional[Dict[Category, int]]
    is_load: bool
    settled: datetime
    local_amount: int
    local_currency: Currency
    updated: datetime
    account_id: AccountID
    user_id: UserID
    counterparty: Union[P2PTransactionCounterparty, FasterPaymentsCounterParty]
    scheme: TransactionScheme
    dedupe_id: DeDupeID
    metadata: Union[P2PTransactionMetadata, FPTransactionMetadata]

    originator: bool
    include_in_spending: bool
    can_be_excluded_from_breakdown: bool
    can_be_made_subscription: bool
    can_split_the_bill: bool
    can_add_to_tab: bool
    amount_is_pending: bool

    fees: Any
    merchant: Any
    labels: Any
    attachments: Any
    international: Any
    atm_fees_detailed: Any


class MonzoSchema(BaseModel):

    class Config:
        extra = "forbid"

    type: str
    data: TransactionCreatedData
