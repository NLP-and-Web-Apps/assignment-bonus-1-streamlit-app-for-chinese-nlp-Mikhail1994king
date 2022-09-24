
import streamlit as st
from snownlp import SnowNLP



st.header("Sentiment Analysis")
with st.expander('情感分析'):
    text = st.text_input("請輸入文字")
    for sen in text:
      st.markdown('**Sentiment Result**')
      s = SnowNLP(sen)
      st.write(list(s.tags))
      st.write(s.sentiments)


    




