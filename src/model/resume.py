
from dataclasses import dataclass
from typing import Optional
@dataclass
class PersonalInfo:
    avatar: str
    first_name: str
    last_name: str
    midle_name: Optional[str]
    title: str
    phone: str
    email: str
    website: Optional[str]
    address: str
    gender: str

    def a():
        print("HELLO")