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

    protein_sequence_id: Optional[ProteinSequence] = Field(
        description="Presented protein sequence", default=None
    )

    dna_database_id: Optional[Database] = Field(
        description="Data base ID", default=None
    )

    dna_database_entry: Optional[str] = Field(
        description="Identifier for the database", default=None
    )

    dna_organism_id: Optional[Organism] = Field(
        description="NCBI Taxonomy ID to identify the organism", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="a1180e99759917986660f7deee422ce5c322f9d3"
    )
