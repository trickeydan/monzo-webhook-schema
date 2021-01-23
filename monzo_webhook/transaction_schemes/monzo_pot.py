"""Transaction Schemas for Monzo Pots."""
from enum import Enum
from typing import NewType, Union

from monzo_webhook.model import Model
from monzo_webhook.types import EntrySetID, UserID

PotID = NewType("PotID", str)
PotAccountID = NewType("PotAccountID", str)
PotDepositID = NewType("PotDepositID", str)
PotWithdrawalID = NewType("PotWithdrawalID", str)


class PotTrigger(Enum):

    USER = "user"


class MonzoPotCounterParty(Model):

    pass  # The counterparty is empty.


class MonzoPotBaseMetadata(Model):

    external_id: str
    pot_account_id: PotAccountID
    pot_id: PotID
    ledger_insertion_id: EntrySetID
    user_id: UserID
    trigger: PotTrigger


class MonzoPotWithdrawalMetadata(MonzoPotBaseMetadata):

    pot_withdrawal_id: PotWithdrawalID


class MonzoPotDepositMetadata(MonzoPotBaseMetadata):

    pot_deposit_id: PotDepositID


MonzoPotMetadata = Union[MonzoPotWithdrawalMetadata, MonzoPotDepositMetadata]
