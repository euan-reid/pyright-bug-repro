from pydantic import Field

from pyright_repro.models.base import MyBaseModel

class Identity(MyBaseModel):
    user: User
    identity_id: str = Field(..., alias='id')
