from fastapi import HTTPException

from repositories import turnos as repo


async def listar_turnos(conn):
    rows = await repo.get_all(conn)
    return [dict(r) for r in rows]


async def obtener_turno(conn, turno_id: int):
    row = await repo.get_by_id(conn, turno_id)
    if not row:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return dict(row)


async def crear_turno(conn, nombre_turno: str, capacidad_maxima: int):
    row = await repo.create(conn, nombre_turno, capacidad_maxima)
    return dict(row)
