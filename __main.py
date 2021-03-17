from databases.core import Database
from fastapi import FastAPI
app = FastAPI()

from typing import List
import databases
import sqlalchemy
from pydantic import BaseModel

DATABASE_URL = 'sqlite:///./test.db'

data = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

# notes = sqlalchemy.Table(
#     "notes"
# )