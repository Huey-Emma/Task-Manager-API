from fastapi import APIRouter, status, HTTPException, Path, Response
from psycopg import errors

from src import schemas
from src.factory import task
from src.misc import exc


router = APIRouter(tags=['Tasks'], prefix='/api/v1/tasks')


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.TaskSchemaOut])
async def fetch_tasks():
    return await task.fetch_all()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.TaskSchemaOut)
async def create_task(payload: schemas.TaskSchemaIn):
    try:
        return await task.create(payload)
    except errors.UniqueViolation:
        raise HTTPException(status.HTTP_409_CONFLICT, 'Task already exist')


@router.get('/{pk}', status_code=status.HTTP_200_OK, response_model=schemas.TaskSchemaOut)
async def fetch_task(pk: int = Path(...)):
    try:
        return await task.fetch_one(pk)
    except exc.NotFound:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Not found')


@router.put('/{pk}', status_code=status.HTTP_200_OK, response_model=schemas.TaskSchemaOut)
async def update_task(*, pk: int = Path(...), payload: schemas.TaskSchemaIn):
    try:
        return await task.update(pk, payload)
    except exc.NotFound:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Not found')


@router.delete('/{pk}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(pk: int = Path(...)):
    try:
        await task.destroy(pk)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except exc.NotFound:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Not found')

