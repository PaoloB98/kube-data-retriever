from pydantic import BaseModel
from typing import List, Optional, Union, Dict, Any
import datetime


class DbBlue(BaseModel):
    id: str
    conf: dict
    input_conf: Optional[dict]
    nsd_: Optional[List[Dict]] = []
    pdu: Optional[List[str]]
    vnfd: Optional[Dict[str, Any]]
    primitives: Optional[List[dict]] = []
    action_to_check: Optional[List[dict]] = []
    timestamp: Dict[str, datetime.datetime] = {}
    config_len: dict = {}
    created: datetime.datetime
    status: str = "bootstraping"
    detailed_status: Union[str, None] = None
    current_operation: Union[str, None] = None
    modified: Optional[datetime.datetime]
    supported_operations: Dict[str, List]
    type: str