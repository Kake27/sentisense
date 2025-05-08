from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/getcsv")
async def get_file():
    if os.path.exists("comments.csv"):
        return FileResponse("comments.csv", filename="output.csv", media_type="text/csv")
    return {"error": "file not found"}