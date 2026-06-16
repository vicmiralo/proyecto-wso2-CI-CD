from pydantic import BaseModel


class TurnoCreate(BaseModel):
    nombre_turno: str
    capacidad_maxima: int
