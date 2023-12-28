import pandas as pd
from langchain.agents import tool
from pydantic.v1 import BaseModel, Field

class latest_movie(BaseModel):
    query: str = Field(..., description= 'User asked for latest movie')

@tool(args_schema=latest_movie)
def get_latest_movies(query:str) -> pd.DataFrame:
    """
    Returns: 다음 영화에서 크롤링한 최신 영화 정보를 리턴한다.
    현재는 그냥 데이터프레임을 넘기지만 나중에 agent화 할 예정.
    """
    
    return pd.read_csv('./data/daum_movie/movie_list.csv')