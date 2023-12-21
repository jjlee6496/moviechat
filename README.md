# moviechat
- RAG, Function calling을 이용한 영화 추천 LLM
## motivation
- Chat GPT 영화 추천 대화 예시
https://chat.openai.com/share/fafd4b02-030d-4b8b-8f89-88adbb985c91
- 위 예시 대화에서 볼 수 있듯이, 최신영화를 물어봤을 때 틀린 정보와 없는 영화 제목을 말하는 hallucination이 일어난다.
- 사용자에게 맞는 영화를 추천하기 위해 langchain을 이용한  영화 추천 LLM을 만들고자 한다.
- 최신영화 정보 등 여러 정보를 받아오기 위해 Function calling을 사용하고 hallucination을 방지하기 위해 RAG pipline과 prompt strategy을 도입하고자 한다.

# Tools

# Data


# To-do
* [] ChatAgent 구현
* [] Tools - weather.py 구현 
* [] Tools - search.py 구현 
* [] streamlit으로 chat 환경 구현