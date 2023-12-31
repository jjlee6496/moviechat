from ChatAgent import ChatAgent
import streamlit as st
from ChatAgent import ChatAgent
# Tools
from Tools.search import get_serpapi_search
from Tools.temperature import get_current_temperature
from Tools.mbti import get_mbti_explaination
from Tools.latest import LatestmovieTool

def UI():
    tools=[get_current_temperature, get_serpapi_search, get_mbti_explaination, LatestmovieTool()]
    chat = ChatAgent(tools=tools)
    
    # Initialize chat history
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
            result = chat.convchain(prompt)['output']
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for t in result:
                full_response += t
                message_placeholder.markdown(t + " ")
            message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    st.title("🎥 Movie Recommendation Chatbot")
    st.caption("영화를 추천해 드립니다")
    UI()