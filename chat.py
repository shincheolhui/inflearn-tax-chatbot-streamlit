import streamlit as st

from dotenv import load_dotenv

from llm import get_ai_response

st.set_page_config(page_title="소득세 챗봇")

st.title("찰리의 소득세 챗봇")
st.caption("소득세에 관련된 모든 것을 답해드립니다!")

load_dotenv()

# Session State also supports attribute based syntax
# Session State가 살아있는 동안 대화내용을 리스트에 저장하기 위함
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

#반복문으로 작성한 content를 화면에 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="소득세에 관련된 궁금한 내용들을 입력해주세요!"):
    #사용자가 입력한 내용을 화면에 출력
    with st.chat_message("user"):
        st.write(user_question)
    #사용자가 입력한 내용을 Session State에 추가
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("AI가 답변 생성 중..."):
        ai_response = get_ai_response(user_question)

        #AI가 입력한 내용을 화면에 출력
        with st.chat_message("ai"):
            # st.write(ai_message) # 답변 생성이 완료되면 화면에 출력
            ai_message = st.write_stream(ai_response) # 타이핑하듯이 답변을 생성하면서 화면에 출력
        #AI가 입력한 내용을 Session State에 추가
        st.session_state.message_list.append({"role": "ai", "content": ai_message})
