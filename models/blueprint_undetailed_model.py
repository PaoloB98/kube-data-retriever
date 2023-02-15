from ipaddress import IPv4Address, IPv4Network
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, conlist


class UndetailedBlueprint(BaseModel):
    id: str
    type: str
    status: str
    detailed_status: Optional[str]
    current_operation: Optional[str]
    created: str
    modified: Optional[str]
    no_areas: int
    no_nsd: int
    no_primitives: int


class UndetailedBlueprintList(BaseModel):
    blueprint_list: List[UndetailedBlueprint]
