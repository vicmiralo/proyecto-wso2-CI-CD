from typing import Optional

import asyncpg
from fastapi import HTTPException

from repositories import turnos as turno_repo
from repositories import usuarios as repo
from schemas.usuario import UsuarioUpdate


async def listar_usuarios(conn):
    rows = await repo.get_all(conn)
    return [dict(r) for r in rows]


async def obtener_usuario(conn, usuario_id: int):
    row = await repo.get_by_id(conn, usuario_id)
    if not row:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return dict(row)


async def crear_usuario(conn, nombre: str, email: str, turno_id: Optional[int]):
    if turno_id is not None:
        turno = await turno_repo.get_by_id(conn, turno_id)
        if not turno:
            raise HTTPException(status_code=400, detail="turno_id no existe")
    try:
        row = await repo.create(conn, nombre, email, turno_id)
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=409, detail="El email ya está registrado")
    return dict(row)


async def actualizar_usuario(conn, usuario_id: int, datos: UsuarioUpdate):
    existing = await repo.get_by_id(conn, usuario_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    nuevo_nombre = datos.nombre if datos.nombre is not None else existing["nombre"]
    nuevo_email = datos.email if datos.email is not None else existing["email"]
    nuevo_turno = datos.turno_id if datos.turno_id is not None else existing["turno_id"]

    try:
        row = await repo.update(conn, usuario_id, nuevo_nombre, nuevo_email, nuevo_turno)
    except asyncpg.UniqueViolationError:
        raise HTTPException(status_code=409, detail="El email ya está registrado")
    return dict(row)


async def eliminar_usuario(conn, usuario_id: int):
    result = await repo.delete(conn, usuario_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
