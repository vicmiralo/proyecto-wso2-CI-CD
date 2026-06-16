import asyncpg


async def get_all(conn: asyncpg.Connection):
    return await conn.fetch("SELECT * FROM turnos ORDER BY id")


async def get_by_id(conn: asyncpg.Connection, turno_id: int):
    return await conn.fetchrow("SELECT * FROM turnos WHERE id = $1", turno_id)


async def create(conn: asyncpg.Connection, nombre_turno: str, capacidad_maxima: int):
    return await conn.fetchrow(
        "INSERT INTO turnos (nombre_turno, capacidad_maxima) VALUES ($1, $2) RETURNING *",
        nombre_turno,
        capacidad_maxima,
    )
