
import streamlit as st
from snownlp import SnowNLP



st.header("Sentiment Analysis")
with st.expander('Analyze text'):
    text = st.text_input("Input screen name")
    if text:
      sent = text.sentences
      s = SnowNLP(sen)
      for sen in sent:
          st.write(s.sentiments)
    




