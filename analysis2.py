
import streamlit as st
from snownlp import SnowNLP



st.header("Sentiment Analysis")
with st.expander('情感分析'):
    text = st.text_input("請輸入文字")
    s1= SnowNLP(text)
    st.markdown("sentiment result")
    for sen in text:
      s = SnowNLP(sen)
      st.write(list(s.tags))
      st.write(s.han)


try:
  st.balloons()
  st.markdown('**Sentence Sentiment Result**')
  st.write(s1.sentiments)
except ValueError as e:
  print(e)








      









