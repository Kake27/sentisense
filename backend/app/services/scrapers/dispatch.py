from app.services.scrapers.youtubescraper import Youtube
from app.services.scrapers.redditscraper import Reddit

def get_comments_for_url(url: str):
    if "youtube.com" in url:
        return Youtube().get_comments(video_url=url)
    # elif "instagram.com" in url:
    #     return Instagram().get_comments(url=url)
    elif "reddit.com" in url:
        return Reddit().get_comments(url=url)
    else:
        raise ValueError("Unsupported URL")
