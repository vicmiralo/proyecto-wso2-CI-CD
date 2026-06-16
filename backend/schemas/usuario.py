from typing import Optional

from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    turno_id: Optional[int] = None


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    turno_id: Optional[int] = None
