from typing import Optional

import asyncpg

_SELECT = """
    SELECT u.id, u.nombre, u.email, t.nombre_turno, t.id AS turno_id
    FROM usuarios u
    LEFT JOIN turnos t ON u.turno_id = t.id
"""


async def get_all(conn: asyncpg.Connection):
    return await conn.fetch(_SELECT + " ORDER BY u.id")


async def get_by_id(conn: asyncpg.Connection, usuario_id: int):
    return await conn.fetchrow(_SELECT + " WHERE u.id = $1", usuario_id)


async def create(conn: asyncpg.Connection, nombre: str, email: str, turno_id: Optional[int]):
    return await conn.fetchrow(
        "INSERT INTO usuarios (nombre, email, turno_id) VALUES ($1, $2, $3) RETURNING *",
        nombre,
        email,
        turno_id,
    )


async def update(
    conn: asyncpg.Connection,
    usuario_id: int,
    nombre: str,
    email: str,
    turno_id: Optional[int],
):
    return await conn.fetchrow(
        "UPDATE usuarios SET nombre=$1, email=$2, turno_id=$3 WHERE id=$4 RETURNING *",
        nombre,
        email,
        turno_id,
        usuario_id,
    )


async def delete(conn: asyncpg.Connection, usuario_id: int) -> str:
    return await conn.execute("DELETE FROM usuarios WHERE id = $1", usuario_id)
