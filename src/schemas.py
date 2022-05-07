import datetime

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    completed: bool


class TaskSchemaOut(TaskSchema):
    id: int
    created_at: datetime.datetime


class TaskSchemaIn(TaskSchema):
    ...
