import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )
    protein_sequence_id: Optional[str] = Field(
        description="Presented protein sequence",
        default=None,
    )

    name: Optional[str] = Field(
        description="Systematic name of the protein.",
        default=None,
    )

    amino_acid_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    database_id: Optional[int] = Field(
        description="Data base ID",
        default=None,
    )

    pdb_id: List[str] = Field(
        description="Identifier for the PDB database",
        default_factory=ListPlus,
    )

    database_entry: Optional[str] = Field(
        description="Identifier for the database",
        default=None,
    )

    organism_id: Optional[int] = Field(
        description="Corresponding organism",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/maxim945/test2.git")
    __commit__: Optional[str] = PrivateAttr(
        default="c56a0a35e0d5a9e18206510331be8b8ccbc5aff5"
    )
