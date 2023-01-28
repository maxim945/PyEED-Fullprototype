import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .proteinsequence import ProteinSequence
from .organism import Organism
from .dnadatabase import DNADatabase


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

    dna_organism_id: Optional[Organism] = Field(
        description="NCBI Taxonomy ID to identify the organism", default=None
    )

    dna_database_id: Optional[DNADatabase] = Field(
        description="Data base ID", default=None
    )

    nucleotide_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="83c6eb115edc9de61b3b418d3f312d152d16509f"
    )
