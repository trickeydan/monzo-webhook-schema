from enum import Enum
from typing import NewType

from monzo_webhook.model import Model
from monzo_webhook.types import EntrySetID

MastercardAuthMessageID = NewType("MastercardAuthMessageID", str)
MastercardCardID = NewType("MastercardCardID", str)
MastercardLifecycleID = NewType("MastercardLifecycleID", str)


class MastercardApprovalType(Enum):

    FULL = "full"


class MastercardCounterParty(Model):

    pass


class MastercardTransactionMetadata(Model):

    ledger_insertion_id: EntrySetID
    mastercard_approval_type: MastercardApprovalType
    mastercard_auth_message_id: MastercardAuthMessageID
    mastercard_card_id: MastercardCardID
    mastercard_lifecycle_id: MastercardLifecycleID
    mcc: str
