
import streamlit as st
from snownlp import SnowNLP



st.header("Sentiment Analysis")
with st.expander('情感分析'):
    text = st.text_input("請輸入文字")
    s1= SnowNLP(text)
    for sen in text:
      s = SnowNLP(sen)
      st.write(list(s.tags))
      st.write(s.han)




try:
  st.balloons()
  st.markdown('**Sentence Sentiment Result**')
  st.write(s1.sentiments)
  if s1.sentiments>0.8:
    st.write("😄")
  elif s1.sentiments>=0.5<0.8:
    st.write("🙂")  
  elif s1.sentiments<0.5:
    st.write("😞")
except ValueError as e:
  print(e)








      









