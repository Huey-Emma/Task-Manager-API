from psycopg.rows import dict_row

from src import schemas
from src.database import pool
from src.misc import exc


async def fetch_all() -> list[schemas.TaskSchemaOut]:
    query_result = None
    with pool.connection() as conn:
        cursor = conn.cursor(row_factory=dict_row)
        qry = 'SELECT id, name, completed, created_at FROM tasks;'
        cursor.execute(qry)
        query_result = cursor.fetchall()
    return [schemas.TaskSchemaOut(**item) for item in query_result]


async def create(payload: schemas.TaskSchemaIn) -> schemas.TaskSchemaOut:
    query_result = None
    with pool.connection() as conn:
        cursor = conn.cursor(row_factory=dict_row)
        qry = """
            INSERT INTO tasks (name, completed) VALUES (%s, %s)
            RETURNING id, name, completed, created_at;
        """
        cursor.execute(qry, (payload.name, payload.completed))
        query_result = cursor.fetchone()
    return schemas.TaskSchemaOut(**query_result)


async def fetch_one(pk: int) -> schemas.TaskSchemaOut:
    query_result = None
    with pool.connection() as conn:
        cursor = conn.cursor(row_factory=dict_row)
        qry = """
            SELECT id, name, completed, created_at
            FROM tasks
            WHERE id = %s;
        """
        cursor.execute(qry, (pk,))
        query_result = cursor.fetchone()
        if not query_result:
            raise exc.NotFound
    return schemas.TaskSchemaOut(**query_result)


async def update(pk: int, payload: schemas.TaskSchemaIn) -> schemas.TaskSchemaOut:
    query_result = None
    with pool.connection() as conn:
        cursor = conn.cursor(row_factory=dict_row)
        qry = """
            UPDATE tasks 
            SET name = %s, completed = %s
            WHERE id = %s
            RETURNING id, name, completed, created_at;
        """
        cursor.execute(qry, (payload.name, payload.completed, pk))
        query_result = cursor.fetchone()
        if not query_result:
            raise exc.NotFound
    return schemas.TaskSchemaOut(**query_result)


async def destroy(pk: int) -> None:
    with pool.connection() as conn:
        cursor = conn.cursor(row_factory=dict_row)
        qry = """
            DELETE FROM tasks
            WHERE id = %s
            RETURNING id;
        """
        cursor.execute(qry, (pk,))
        if not cursor.fetchone():
            raise exc.NotFound
