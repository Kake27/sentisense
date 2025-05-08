from fastapi import APIRouter, BackgroundTasks
from app.services.status import get_status
from app.services.runanalysis import run_analysis

router = APIRouter()

@router.get("/analyse")
async def analyse(url: str, background_tasks: BackgroundTasks):
    status = get_status()
    if status["processing"]:
        return {"message": "Already processing"}
    if url == status["prev_url"] and status["file_created"]:
        return {"file_created": True}
    
    background_tasks.add_task(run_analysis, url)
    return {"message": "Analysis started"}