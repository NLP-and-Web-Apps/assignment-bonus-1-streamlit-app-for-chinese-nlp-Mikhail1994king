
import streamlit as st
from snownlp import SnowNLP



st.header("Sentiment Analysis")
with st.expander('Analyze text'):
    text = st.text_input("Input screen name")
    for sen in text:
      s = SnowNLP(sen)
      st.write(s.sentiments)
    




