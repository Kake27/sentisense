from fastapi import APIRouter, HTTPException
import os
import pandas as pd

router = APIRouter()
@router.get("/graphs")
async def get_graph_data():
    if(os.path.exists("comments.csv")):
        df  = pd.read_csv("comments.csv")
        sentiment_count = df["Sentiment"].value_counts().to_dict()
        return sentiment_count
    return {"error": "file not found"}