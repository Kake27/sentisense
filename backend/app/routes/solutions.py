from fastapi import APIRouter
import os
import pandas as pd
import json
from app.services.gemini import Genai
from app.services.clusters.clustermodel import Clustering
from app.services.status import update_status

genai = Genai()
clustering = Clustering()

router = APIRouter()
@router.get("/solutions")
async def get_solutions():
    try:
        solution_data = ""
        if(os.path.exists("comments.csv")):
            df = pd.read_csv("comments.csv")
            solution_data = clustering.create_cluster(df)
        else:
            update_status(error=True)
            return {"error": "File not found"}

        data = json.loads(solution_data)
        formatted_output = ""

        for sentiment, clusters in data.items():
            formatted_output += f"\nSentiment: {sentiment.lower()}\n"
            for cluster, comments in clusters.items():
                formatted_output += f"Cluster {cluster}: {comments}\n"

        # print(formatted_output)

        
        solutions = genai.get_solutions(
            prompt=
            """
                Analyze the following clusters of product reviews categorized by sentiment (neutral, negative, positive).

            For each sentiment (neutral, negative, positive), provide bullet points (maximum 10 words for each bullet) for:
            1. How to improve neutral sentiments.
            2. How to minimize negative sentiments.
            3. How to enhance positive sentiments.

            Data: """ + formatted_output + 
            """
            Return: Provide only the bullet points for improving neutral reviews, minimizing negative reviews, and enhancing positive reviews. 
            Always give the output in the format given here:
            {
                "Neutral": [
                    "Prompt engagement with questions about the content.",
                    "Add visually stimulating elements to capture attention.",
                    "Relate content to broader, interesting stories/movies.",
                    "Provide more facts/interesting info to increase engagement."
                ],
                "Negative": [
                    "Clearly explain the logic of events portrayed.",
                    "Be realistic about chances for promotion participation.",
                    "Ensure content is high quality and enjoyable.",
                    "Avoid plot holes or confusing aspects in content."
                ],
                "Positive": [
                    "Continue high animation/modeling quality.",
                    "Show the process in behind-the-scenes videos.",
                    "Expand the breadth of knowledge shared in videos.",
                    "Encourage viewers to express feelings."
                ]
            }
            """
        )
        return solutions
    
    except Exception as e:
        print("Error occurred while fetching solutions: "+ str(e))
        return {"error":e}