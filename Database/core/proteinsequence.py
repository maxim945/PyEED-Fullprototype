import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .database import Database
from .organism import Organism


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )

    protein_sequence_id: Optional[str] = Field(
        description="Presented protein sequence", default=None
    )

    name: Optional[str] = Field(
        description="Systematic name of the protein.", default=None
    )

    amino_acid_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    protein_database_id: Optional[Database] = Field(
        description="Data base ID", default=None
    )

    protein_organism_id: Optional[Organism] = Field(
        description="Corresponding organism", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8fff177c7149599ef54caa3cd8c4dd875284a127"
    )
