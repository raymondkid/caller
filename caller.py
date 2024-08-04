import streamlit as st
from anthropic import Anthropic

# Streamlit 앱 설정
st.set_page_config(page_title="CALLER", page_icon=":brain:")
st.title("CALLER")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# API 키 입력
api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")

if api_key:
    anthropic = Anthropic(api_key=api_key)

    # 사용자 입력
    user_input = st.text_input("질문을 입력하세요:")

    if user_input:
        # 메시지 추가
        st.session_state.messages.append({"role": "human", "content": user_input})

        # Claude에 요청
        response = anthropic.completions.create(
            model="claude-3-sonnet-20240229",
            max_tokens_to_sample=1000,
            prompt=f"Human: {user_input}\n\nAssistant: ",
        )

        # 응답 추가
        st.session_state.messages.append({"role": "assistant", "content": response.completion})

    # 대화 내용 표시
    for message in st.session_state.messages:
        if message["role"] == "human":
            st.write(f"**You:** {message['content']}")
        else:
            st.write(f"**Assistant:** {message['content']}")

else:
    st.warning("API 키를 입력해주세요.")
