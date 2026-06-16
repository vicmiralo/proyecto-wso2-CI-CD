from fastapi import APIRouter, Depends

from database import get_conn
from schemas.usuario import UsuarioCreate, UsuarioUpdate
from views import usuarios as view

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("")
async def listar_usuarios(conn=Depends(get_conn)):
    return await view.listar_usuarios(conn)


@router.get("/{usuario_id}")
async def obtener_usuario(usuario_id: int, conn=Depends(get_conn)):
    return await view.obtener_usuario(conn, usuario_id)


@router.post("", status_code=201)
async def crear_usuario(usuario: UsuarioCreate, conn=Depends(get_conn)):
    return await view.crear_usuario(conn, usuario.nombre, usuario.email, usuario.turno_id)


@router.patch("/{usuario_id}")
async def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate, conn=Depends(get_conn)):
    return await view.actualizar_usuario(conn, usuario_id, datos)


@router.delete("/{usuario_id}", status_code=204)
async def eliminar_usuario(usuario_id: int, conn=Depends(get_conn)):
    await view.eliminar_usuario(conn, usuario_id)
