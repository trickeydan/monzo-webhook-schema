"""Monzo Webhook Schema."""
from datetime import datetime
from typing import Any, Dict, Optional

from .model import Model
from .transaction_schemes import (Counterparty, TransactionMetadata,
                                  TransactionScheme)
from .types import (AccountID, Category, Currency, DeDupeID, TransactionID,
                    UserID)


class TransactionCreatedData(Model):

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
    counterparty: Counterparty
    scheme: TransactionScheme
    dedupe_id: DeDupeID
    metadata: TransactionMetadata

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


class MonzoWebhookSchema(Model):

    type: str
    data: TransactionCreatedData
