import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class DNADatabase(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dnadatabaseINDEX"),
        xml="@id",
    )

    database: Optional[int] = Field(
        description="Position in the sequence where the domain starts", default=None
    )

    link_to_database: Optional[int] = Field(
        description="Position in the sequence where the domain ends", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="ee7c680c49c24eb57321730935a931d1151e6541"
    )
