from fastapi import APIRouter
from app.services.status import get_status

router = APIRouter()

@router.get("/status")
async def status():
    return get_status()
