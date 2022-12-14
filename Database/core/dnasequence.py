import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .proteinsequence import ProteinSequence
from .database import Database
from .organism import Organism


@forge_signature
class DNASequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("dnasequenceINDEX"),
        xml="@id",
    )

    dna_sequence_id: Optional[str] = Field(
        description=(
            "Reference to the Translated DNA from the matching Protein sequence"
        ),
        default=None,
    )

    database_entry: Optional[str] = Field(
        description="Identifier for the database", default=None
    )

    protein_sequence_id: Optional[ProteinSequence] = Field(
        description="Presented protein sequence", default=None
    )

    database_id: Optional[Database] = Field(description="Data base ID", default=None)

    organism_id: Optional[Organism] = Field(
        description="NCBI Taxonomy ID to identify the organism", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="ac4e18bea4449d007023939606bfc5ad7737c2d4"
    )
