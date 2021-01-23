from datetime import datetime
from typing import NewType

from pydantic import ConstrainedFloat, ConstrainedStr, HttpUrl

from .model import Model
from .types import Category, TransactionID

MerchantID = NewType("MerchantID", str)
MerchantGroupID = NewType("MerchantGroupID", str)


class Latitude(ConstrainedFloat):

    ge = -90
    le = 90


class Longitude(ConstrainedFloat):

    ge = -180
    le = 180


class MerchantAddress(Model):

    short_formatted: str
    formatted: str
    address: str
    city: str
    region: str
    country: str
    postcode: str
    latitude: Latitude
    longitude: Longitude
    zoom_level: int
    approximate: bool


class MerchantMetadata(Model):

    created_for_merchant: MerchantID
    created_for_transaction: TransactionID
    enriched_from_settlement: TransactionID
    foursquare_id: str
    foursquare_website: str
    google_places_icon: str
    google_places_id: str
    google_places_name: str
    suggested_tags:  str
    twitter_id: str
    website: str


class Emoji(ConstrainedStr):

    max_length = 1
    min_length = 1


class Merchant(Model):

    id: MerchantID
    group_id: MerchantGroupID
    created: datetime
    name: str
    logo: HttpUrl
    emoji: Emoji
    category: Category
    online: bool
    atm: bool
    address: MerchantAddress
    updated: datetime
    metadata: MerchantMetadata
    disable_feedback: bool
