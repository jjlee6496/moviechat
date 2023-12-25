import re
from serpapi import GoogleSearch
from pydantic.v1 import BaseModel, Field
from langchain.agents import tool
from utils import get_serp_api_key

# Define the input schema
class SearchInput(BaseModel):
    query: str = Field(..., description="Search using Google when user ask for more information about the movie")

serpapi_key = get_serp_api_key()

# 결과를 예쁘게 받아오기 위해 패턴 매칭으로 필요없는 정보 제거
def filter_dict(dictionary, exclude_patterns):
    if not isinstance(dictionary, dict):
        return dictionary

    filtered = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            filtered[key] = filter_dict(value, exclude_patterns)
        elif isinstance(value, list):
            filtered[key] = [filter_dict(item, exclude_patterns) for item in value]
        else:
            if not any(re.search(pattern, key) for pattern in exclude_patterns):
                filtered[key] = value
    return filtered

exclude_patterns = [r'links', r'image', r'link', r'source', r'extensions']

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
    final_result = dict({"search_results": results['knowledge_graph']})
    if results.get('top_stories'):
        final_result['latest_news'] = results['top_stories']
    
    return filter_dict(final_result, exclude_patterns)