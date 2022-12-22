import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Standard(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("standardINDEX"),
        xml="@id",
    )

    standard_numering_scheme_id: Optional[int] = Field(
        description="Equivalent position in the reference sequence", default=None
    )

    standard_numering_scheme_name: Optional[int] = Field(
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
        default=None,
    )

    protein_sequence_id: Optional[str] = Field(
        description="Presented protein sequence", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="e1211dd853b8bac271228f1380defc53d6ea7aa9"
    )
