"""Base Pydantic Model to ensure consistency of settings."""

from pydantic import BaseModel


class Model(BaseModel):

    class Config:

        extra = "forbid"  # Don't allow spurious attributes.
