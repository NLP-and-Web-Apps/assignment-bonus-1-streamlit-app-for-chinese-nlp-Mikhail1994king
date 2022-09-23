
import pandas as pd
import numpy as np
import streamlit as st
from snownlp import SnowNLP

st.header("Sentiment Analysis")
with st.expander('Analyze text'):
    text = st.text_input("Input screen name")

def SnowNLP(text):
  sent = text.sentences
  for sen in sent:
      s = SnowNLP(sen)
      print(s.sentiments)

SnowNLP
st.write(pd.DataFrame({
  'first column': [s],
}))

