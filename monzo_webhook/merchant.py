from datetime import datetime
from typing import NewType

from pydantic import constr, confloat, HttpUrl

MerchantID = NewType("MerchantID", str)
MerchantGroupID = NewType("MerchantGroupID", str)

from .model import Model
from .types import Category, TransactionID


class MerchantAddress(Model):
    
    short_formatted: str
    formatted: str
    address: str
    city: str
    region: str
    country: str
    postcode: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
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


class Merchant(Model):
    
    id: MerchantID
    group_id: MerchantGroupID
    created: datetime
    name: str
    logo: HttpUrl
    emoji: constr(max_length=1, min_length=1)
    category: Category
    online: bool
    atm: bool
    address: MerchantAddress
    updated: datetime
    metadata: MerchantMetadata
    disable_feedback: bool
