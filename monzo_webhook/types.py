from enum import Enum
from typing import NewType

from pydantic import ConstrainedStr

__all__ = [
    "Category",
    "AccountID",
    "DeDupeID",
    "UserID",
    "TransactionID",
    "EntrySetID",
    "Currency",
    "BeneficiaryAccountType",
]

Category = NewType("Category", str)
AccountID = NewType("AccountID", str)
DeDupeID = NewType("DeDupeID", str)
UserID = NewType("UserID", str)
TransactionID = NewType("TransactionID", str)
EntrySetID = NewType("EntrySetID", str)


class Currency(Enum):

    GBP = "GBP"


class BeneficiaryAccountType(Enum):

    PERSONAL = "Personal"


class EmptyStr(ConstrainedStr):

    max_length = 0
    min_length = 0
