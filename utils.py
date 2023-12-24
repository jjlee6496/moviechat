import os 
from dotenv import load_dotenv, find_dotenv

def get_openai_api_key():
    _ = load_dotenv(find_dotenv())
    return os.getenv("OPENAI_API_KEY")

# 검색 결과가 달라서 사용 불가
# def get_naver_api_key():
#     _ = load_dotenv(find_dotenv())
#     return os.getenv("NAVER_CLIENT_ID"), os.getenv("NAVER_CLIENT_SECRET")


def get_serp_api_key():
    _ = load_dotenv(find_dotenv())
    return os.getenv("SERPAPI_KEY")
