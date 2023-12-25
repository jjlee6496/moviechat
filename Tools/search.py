from serpapi import GoogleSearch
from pydantic.v1 import BaseModel, Field
from langchain.agents import tool
from utils import get_serp_api_key

# Define the input schema
class SearchInput(BaseModel):
    query: str = Field(..., description="Search using Google when user ask for more information about the movie")

serpapi_key = get_serp_api_key()

@tool(args_schema=SearchInput)
def get_serpapi_search(query: str) -> dict:
    """serpapi search API를 활용하여 관련 정보와 관련 뉴스를 반환하는 함수

    Args:
        query (str): 검색할 키워드

    Returns:
        dict: 검색 결과 dict로 반환
    """
    params = {
        "api_key": serpapi_key,
        "engine": "google",
        "q": query,
        "location": "Seoul, Seoul, South Korea",
        "google_domain": "google.co.kr",
        "gl": "kr",
        "hl": "ko"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    return dict({"search_results": results['knowledge_graph'], "related_news": results['top_stories']})