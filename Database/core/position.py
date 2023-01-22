import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .proteinsequence import ProteinSequence


@forge_signature
class Position(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("positionINDEX"),
        xml="@id",
    )

    position_id: Optional[int] = Field(
        description="Equivalent position in the reference sequence", default=None
    )

    standard_numbering_scheme_id: Optional[int] = Field(
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
        default=None,
    )

    annotation_id: Optional[int] = Field(
        description=(
            "Function that is found in the annotated amino acid or sub-sequence"
        ),
        default=None,
    )

    protein_sequence_id: Optional[ProteinSequence] = Field(
        description=(
            "Position that is equivalent to the reference sequence position that is"
            " also given"
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="5f478252c20ad26b00aea4398303bac3b2152647"
    )
