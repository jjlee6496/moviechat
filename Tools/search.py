import requests
from pydantic.v1 import BaseModel, Field
from langchain.agents import tool
from utils import get_serp_api_key

# Define the input schema
class SearchInput(BaseModel):
    query: str = Field(..., description="Search using Google what user asked for")

serpapi_key = get_serp_api_key()

@tool(args_schema=SearchInput)
def get_serpapi_search(query: str) -> dict:
    """serpapi search API를 활용한 영화 검색결과 반환 함수

    Args:
        query (str): 검색할 키워드

    Returns:
        dict: 검색 결과 dict로 반환
    """
    url = f"https://serpapi.com/search.json?q={query}&api_key={serpapi_key}"
    response = requests.get(url)
    if response.status_code == 200:
        search_results = response.json()
        print(search_results)
    else:
        print(f"Request failed with status code: {response.status_code}")
    
    return search_results