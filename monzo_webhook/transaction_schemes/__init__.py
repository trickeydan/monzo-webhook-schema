from enum import Enum
from typing import Union

from .faster_payments import FasterPaymentsCounterParty, FPTransactionMetadata
from .monzo_pot import MonzoPotCounterParty, MonzoPotMetadata
from .p2p import P2PTransactionCounterparty, P2PTransactionMetadata

__all__ = [
    "Counterparty",
    "TransactionMetadata",
    "TransactionScheme",
]


class TransactionScheme(Enum):

    P2P = "p2p_payment"
    POT = "uk_retail_pot"
    FASTER_PAYMENTS = "payport_faster_payments"


Counterparty = Union[
    P2PTransactionCounterparty,
    MonzoPotCounterParty,
    FasterPaymentsCounterParty,
]
TransactionMetadata = Union[
    P2PTransactionMetadata,
    MonzoPotMetadata,
    FPTransactionMetadata,
]
