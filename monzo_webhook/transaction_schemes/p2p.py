"""
P2P Transaction Schemas

P2P is the transaction type used when sending and receiving between
accounts that are both Monzo Users.
"""
from enum import Enum
from typing import NewType

from monzo_webhook.model import Model
from monzo_webhook.types import AccountID, UserID

P2PTransferID = NewType("P2PTransferID", str)
TabID = NewType("TabID", str)


class P2PInitiator(Enum):

    TAB = "tab"


class P2PTransactionCounterparty(Model):

    account_id: AccountID
    name: str
    preferred_name: str
    user_id: UserID


class P2PTransactionMetadata(Model):

    p2p_initiator: P2PInitiator
    p2p_transfer_id: P2PTransferID
    tab_id: TabID
