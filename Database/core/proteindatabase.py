import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ProteinDatabase(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteindatabaseINDEX"),
        xml="@id",
    )

    database: Optional[str] = Field(
        description="Position in the sequence where the domain starts", default=None
    )

    link_to_database: Optional[str] = Field(
        description="Position in the sequence where the domain ends", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="83c6eb115edc9de61b3b418d3f312d152d16509f"
    )
