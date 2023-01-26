from sqlmodel import SQLModel, Field

class Peak(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    lat: float
    lon: float 
    altitude: float 
    name: str
