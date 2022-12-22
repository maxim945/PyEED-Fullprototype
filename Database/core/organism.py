import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Organism(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("organismINDEX"),
        xml="@id",
    )

    organism_id: Optional[str] = Field(
        description="NCBI Taxonomy ID to identify the organism", default=None
    )

    organism_name: Optional[str] = Field(description="Organism name", default=None)

    ncbi_taxonomy_id: Optional[str] = Field(
        description="NCBI Taxonomy ID to identify the organism", default=None
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/maxim945/test2.git")

    __commit__: Optional[str] = PrivateAttr(
        default="5600128b772670b3f846f963e6299b065f6d129f"
    )
