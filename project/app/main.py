from fastapi import Depends, FastAPI
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Peak

app = FastAPI()

@app.get("/peaks", response_model=list[Peak])
async def get_peaks(
    session: AsyncSession = Depends(get_session)
) -> list:
    peaks = await session.execute(select(Peak))
    return [*peaks.scalars().all()]

@app.post("/peak")
async def add_peak(
    peak: Peak, session: AsyncSession = Depends(get_session)
) -> Peak:
    session.execute(
        insert(Peak).values(**peak.dict())
    )
    session.add(peak)
    await session.commit()
    return peak

@app.put("/peak/{peak_id}")
async def update_peak(
    peak: Peak, peak_id: int, session: AsyncSession = Depends(get_session)
) -> Peak:
    peak.id = peak_id
    await session.execute(
        update(Peak)
        .where(Peak.id == peak_id).values(**peak.dict())
    )
    await session.commit()
    return peak


@app.delete("/peak/{peak_id}")
async def del_peak(
    peak_id: int, session: AsyncSession = Depends(get_session)
) -> str:
    pak = await session.execute(select(Peak).where(Peak.id==peak_id))
    peak_to_delete = pak.scalars().first()
    if peak_to_delete:
        await session.delete(peak_to_delete)
        await session.commit()
    else :
        return "Id not found in database"
    return f"Peak with id={peak_id} is deleted"
