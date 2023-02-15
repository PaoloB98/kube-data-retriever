from typing import List, Optional

from pydantic import BaseModel
class K8sCluster(BaseModel):
    name: str
    provided_by: str
    blueprint_ref: Optional[str]
    credentials: str
    vim_name: str
    k8s_version: str
    networks: Optional[List[str]]
    areas: List[int]
    cni: Optional[str]
    nfvo_status: Optional[str]