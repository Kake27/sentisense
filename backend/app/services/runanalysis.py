import os
import pandas as pd
from app.services.scrapers.dispatch import get_comments_for_url
from app.models.model_loader import SentimentAnalysis
from app.services.status import update_status

def run_analysis(url: str):
    update_status(processing=True, error=False, file_created=False, comments_found=False, prev_url=url)

    if os.path.exists("comments.csv"):
        os.remove("comments.csv")

    try:
        comments = get_comments_for_url(url)
        update_status(comments_found=True)

        analyzer = SentimentAnalysis()
        sentiments = [(comment, analyzer.predict_class([comment])) for comment in comments]

        pd.DataFrame(sentiments, columns=["Comment", "Sentiment"]).to_csv("comments.csv", index=False)
        update_status(file_created=True)

    except Exception as e:
        update_status(error=True)
        print(f"Error during analysis: {e}")
    finally:
        update_status(processing=False)