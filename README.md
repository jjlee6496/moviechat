# moviechat
- RAG, Function calling을 이용한 영화 추천 LLM  
- [블로그 글 1](https://velog.io/@jjlee6496/LangChain%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%98%81%ED%99%94-%EC%B6%94%EC%B2%9C%EA%B8%B0-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%80-1)  

## motivation
- Chat GPT 영화 추천 대화 예시
https://chat.openai.com/share/fafd4b02-030d-4b8b-8f89-88adbb985c91
- 위 예시 대화에서 볼 수 있듯이, 최신영화를 물어봤을 때 틀린 정보와 없는 영화 제목을 말하는 hallucination이 일어난다.
- 사용자에게 맞는 영화를 추천하기 위해 langchain을 이용한  영화 추천 LLM을 만들고자 한다.
- 최신영화 정보 등 여러 정보를 받아오기 위해 Function calling을 사용하고 hallucination을 방지하기 위해 RAG pipline과 prompt strategy을 도입하고자 한다.

# Tools
## [temperature.py](https://github.com/jjlee6496/moviechat/blob/main/Tools/temperature.py)
* OpenAPI로 위도와 경도를 입력 받으면 그 지역의 기온을 알려주는 함수
## [search.py](https://github.com/jjlee6496/moviechat/blob/main/Tools/search.py)
* SerpAPI를 사용하여 입력된 검색어에 대한 검색 결과를 리턴하는 함수
## [latest.py](https://github.com/jjlee6496/moviechat/blob/main/Tools/latest.py)
* 크롤링으로 수집해둔 최신영화(Daum영화 예매율) 정보를 리턴해주는 함수
## [mbti.py](https://github.com/jjlee6496/moviechat/blob/main/Tools/mbti.py)
* Mbti 정보를 context에 더해 성격에 맞는 영화를 추천해주기 위해 PromptTemplate로 mbti에 대한 설명을 리턴해주는 함수
# Data Source
- [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
- [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) - rating이 없어서 사용 보류
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [Daum 영화 예매율](https://movie.daum.net/ranking/reservation)


# To-do
* [X] Tools - temperature.py 구현 
* [X] Tools - search.py 구현
* [x] Tools - search.py 검색결과 정제(길이 줄이기 및 예외처리)
* [X] Tools - mbti.py 구현
* [ ] RAG pipline 추가 - 보류
* [ ] Chain fallbacks 처리
* [ ] ChatAgent 구현 - 메모리 사용해서 이전 대화 기억하도록
* [ ] streamlit front