import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Organism(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("organismINDEX"),
        xml="@id",
    )
    organism_id: Optional[str] = Field(
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

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/maxim945/test2.git")
    __commit__: Optional[str] = PrivateAttr(
        default="c56a0a35e0d5a9e18206510331be8b8ccbc5aff5"
    )
