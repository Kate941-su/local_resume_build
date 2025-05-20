
from dataclasses import dataclass
from typing import Optional
@dataclass
class PersonalInfo:
    image_path: str
    first_name: str
    last_name: str
    middle_name: Optional[str]
    title: str
    phone: str
    email: str
    website: Optional[str]
    address: str
    gender: str

    def debug_print(self):
        print(f"Image Path: {self.image_path}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Middle Name: {self.middle_name}")
        print(f"Title: {self.title}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Website: {self.website}")
        print(f"Address: {self.address}")
        print(f"Gender: {self.gender}")

@dataclass
class ResumeData:
    personal_info: PersonalInfo