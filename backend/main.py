import os
from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI

from routers import turnos, usuarios

DB_DSN = os.environ.get("DB_DSN", "postgresql://postgres:postgres@db:5432/postgres")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pool = await asyncpg.create_pool(DB_DSN)
    yield
    await app.state.pool.close()


app = FastAPI(title="Gestión de Turnos", lifespan=lifespan)

app.include_router(usuarios.router)
app.include_router(turnos.router)
