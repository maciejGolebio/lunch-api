from abc import ABC
from pydantic import BaseModel
from tinydb import TinyDB


class TinyDBBase(ABC):
    def __init__(self, client: TinyDB):
        self.client = client
