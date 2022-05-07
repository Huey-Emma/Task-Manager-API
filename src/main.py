from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import pool
from src.routes import task


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE']
)


@app.on_event('startup')
def connect_database():
    pool.open()

    with pool.connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER GENERATED ALWAYS AS IDENTITY, 
                name VARCHAR NOT NULL, 
                completed BOOLEAN NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT now(), 
                PRIMARY KEY(id), 
                CONSTRAINT unique_name UNIQUE(name)
            );
        """)


app.include_router(task.router)


@app.on_event('shutdown')
def disconnect_database():
    pool.close()
