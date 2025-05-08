from fastapi import APIRouter, HTTPException
import os
import pandas as pd
from app.services.clusters.clustermodel import Clustering

router = APIRouter()
clustering = Clustering()

@router.get("/clustering")
async def get_clustering():
    if(os.path.exists("comments.csv")):
        df = pd.read_csv("comments.csv")
        
        # return {"message": "testing clusters"}
        
        clusters = clustering.create_cluster(df)
        return clusters
    
    return {"error": "File not found"}
