from app.models.webpage import Webpage


def get_webpage(webpage: str) -> None:
    
    return Webpage.get_metadata(webpage_url=webpage)