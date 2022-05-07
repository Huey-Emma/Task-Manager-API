from psycopg_pool import ConnectionPool

from src.config import settings

conninfo = f'dbname={settings.db_name} user={settings.db_username} password={settings.db_password} host={settings.db_host}'
pool = ConnectionPool(conninfo, open=False)
