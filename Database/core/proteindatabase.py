import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class ProteinDatabase(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteindatabaseINDEX"),
        xml="@id",
    )
    database_id: Optional[str] = Field(
        description="Name of the annotated domain",
        default=None,
    )

    database: Optional[int] = Field(
        description="Position in the sequence where the domain starts",
        default=None,
    )

    link_to_database: Optional[int] = Field(
        description="Position in the sequence where the domain ends",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="35a45da72b076b37d11cbe19c2754ecba341f7f3"
    )
