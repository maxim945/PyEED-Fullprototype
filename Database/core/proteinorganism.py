import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class ProteinOrganism(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinorganismINDEX"),
        xml="@id",
    )
    organism_id: Optional[int] = Field(
        description="NCBI Taxonomy ID to identify the organism",
        default=None,
    )

    organism_name: Optional[str] = Field(
        description="Organism name",
        default=None,
    )

    ncbi_taxonomy_id: Optional[str] = Field(
        description="NCBI Taxonomy ID to identify the organism",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="35a45da72b076b37d11cbe19c2754ecba341f7f3"
    )
