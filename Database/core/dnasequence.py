import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class DNASequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dnasequenceINDEX"),
        xml="@id",
    )
    protein_sequence_id: str = Field(
        ...,
        description="Presented protein sequence",
    )

    dna_sequence_id: Optional[str] = Field(
        description=(
            "Reference to the Translated DNA from the matching Protein sequence"
        ),
        default=None,
    )

    database_id: Optional[int] = Field(
        description="Data base ID",
        default=None,
    )

    database_entry: Optional[str] = Field(
        description="Identifier for the database",
        default=None,
    )

    organism_id: Optional[int] = Field(
        description="NCBI Taxonomy ID to identify the organism",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/maxim945/test2.git")
    __commit__: Optional[str] = PrivateAttr(
        default="2659f3bcd1129f2baa181f813c99563a59096644"
    )
