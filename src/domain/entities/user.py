from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: str
    full_name: str
    username: str
    password: str
    created_at: datetime
