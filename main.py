from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

#ChatOpenAI 초기화
llm = init_chat_model("gpt-4o-mini", temperature=0.01)

#Prompt Template 생성
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "{input}"),
    ]
)

#문자열 출력 파서
output_parser = StrOutputParser()

# LLM Chain 구성
chain = prompt | llm | output_parser

# LLM Chain 실행
#content = "중년"
#result = chain.invoke({"input": content +"에 대해 시를 써줘"})
#print(result)

st.title("AI 시인")
content = st.text_input("시의 주제를 제시해주세요")
st.write("시의 주제는, " + content)
if st.button("시 작성 요청하기"):
    with st.spinner("Wait for it...", show_time=True):
        result = chain.invoke({"input": content + "에 대해 시를 써줘"})
        st.write(result)
