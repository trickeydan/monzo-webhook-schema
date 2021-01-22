from enum import Enum
from typing import Union

from .faster_payments import FasterPaymentsCounterParty, FPTransactionMetadata
from .p2p import P2PTransactionCounterparty, P2PTransactionMetadata

__all__ = [
    "Counterparty",
    "TransactionMetadata",
    "TransactionScheme",
]


class TransactionScheme(Enum):

    P2P = "p2p_payment"
    FASTER_PAYMENTS = "payport_faster_payments"


Counterparty = Union[P2PTransactionCounterparty, FasterPaymentsCounterParty]
TransactionMetadata = Union[P2PTransactionMetadata, FPTransactionMetadata]
