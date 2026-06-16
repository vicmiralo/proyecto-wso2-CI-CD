from fastapi import APIRouter, Depends

from database import get_conn
from schemas.turno import TurnoCreate
from views import turnos as view

router = APIRouter(prefix="/turnos", tags=["Turnos"])


@router.get("")
async def listar_turnos(conn=Depends(get_conn)):
    return await view.listar_turnos(conn)


@router.get("/{turno_id}")
async def obtener_turno(turno_id: int, conn=Depends(get_conn)):
    return await view.obtener_turno(conn, turno_id)


@router.post("", status_code=201)
async def crear_turno(turno: TurnoCreate, conn=Depends(get_conn)):
    return await view.crear_turno(conn, turno.nombre_turno, turno.capacidad_maxima)
