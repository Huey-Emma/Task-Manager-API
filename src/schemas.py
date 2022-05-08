import datetime
from typing import Optional

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    completed: Optional[bool] = True


class TaskSchemaOut(TaskSchema):
    id: int
    created_at: datetime.datetime


class TaskSchemaIn(TaskSchema):
    ...
