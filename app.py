import openai
from langchain.chat_models import ChatOpenAI
from langchain.tools.render import format_tool_to_openai_function
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.prompts import MessagesPlaceholder
from langchain.schema.runnable import RunnablePassthrough
from langchain.memory import ConversationBufferWindowMemory
from langchain.agents.format_scratchpad import format_to_openai_functions
from prompts import *

# Tools
from Tools.search import get_serpapi_search
from Tools.temperature import get_current_temperature
from Tools.mbti import get_mbti_explaination
from Tools.latest import LatestmovieTool

# utils
from utils import get_openai_api_key
import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory

tools=[get_current_temperature, get_serpapi_search, get_mbti_explaination, LatestmovieTool()]

openai.api_key = get_openai_api_key()
memory = ConversationBufferWindowMemory(return_messages=True, memory_key='chat_history', input_key='prompt', k=5)
functions = [
        format_tool_to_openai_function(f) for f in [get_current_temperature, get_serpapi_search, get_mbti_explaination]
]

prompt1 = ChatPromptTemplate.from_messages([
    ("system", prompt1_system),
    MessagesPlaceholder(variable_name='chat_history'),
    ("user", "{prompt}"),
    MessagesPlaceholder(variable_name='agent_scratchpad')
])

model = ChatOpenAI(temperature=0.4).bind(functions=functions)
retrieval_chain = RunnablePassthrough.assign(
    agent_scratchpad = lambda x: format_to_openai_functions(x["intermediate_steps"])
) | prompt1 | model | OpenAIFunctionsAgentOutputParser()

agent_executor = AgentExecutor(agent=retrieval_chain, tools=[get_current_temperature, get_serpapi_search, get_mbti_explaination, LatestmovieTool()], memory=memory, verbose=True)

# Chat UI
st.title("🎥 Movie Recommendation Chatbot")
st.caption("영화를 추천해 드립니다")
# Initialize chat history

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
msgs = StreamlitChatMessageHistory()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("최신 영화 추천해줘"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner('정보를 찾는 중..'):
        st_callback = StreamlitCallbackHandler(st.container())
        result = agent_executor({"prompt": prompt, "mbti_list": mbti_list, "recommend_format":recommend_format},callbacks=[st_callback])['output']
        st.session_state['chat_history'] = 
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown(result)
    # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": result})