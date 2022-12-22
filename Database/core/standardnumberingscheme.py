import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .proteinsequence import ProteinSequence


@forge_signature
class StandardNumberingScheme(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("standardnumberingschemeINDEX"),
        xml="@id",
    )
    standard_numering_scheme_id: Optional[int] = Field(
        description="Equivalent position in the reference sequence",
        default=None,
    )

    standard_numering_scheme_name: Optional[int] = Field(
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
        default=None,
    )

    protein_sequence_id: Optional[ProteinSequence] = Field(
        description="Presented protein sequence",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="54a1503ced69fed995f2afae6657bb6ed2bef492"
    )