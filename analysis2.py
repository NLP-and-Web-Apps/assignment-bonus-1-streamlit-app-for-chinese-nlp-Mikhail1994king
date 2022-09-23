import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import os
import streamlit as st


consumer_key= 'bPrBRQsuST1smGOYTOTI6iCY0'
consumer_secret= 'MpWtjY30KOzjDaa1w1Asu81FTRw7BF4US3SKPgxyHylr9kh63A'
access_token= '1549064619041640448-Xr9SqMJfUrsXBsD9otYhF0sOxGqH1L'
access_token_secret= '71L41fJAghPgABrqpTD9CrPFMcxo5xUAbWFS1NYZz1zAa'

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
# Set the access token and access token secret
authenticate.set_access_token(access_token, access_token_secret) 
    
# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)


st.header("Sentiment Analysis")
with st.expander('Analyze text'):
    text = st.text_input("Input screen name")

posts = api.user_timeline(screen_name="@iingwen", count = 100, lang ="eng", tweet_mode="extended")
for tweet in posts[:5]:
    print(str(i) +') '+ tweet.full_text + '\n')
    i= i+1

st.write(pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets']))
# Show the first 5 rows of data
st.df()





def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
 text = re.sub('#', '', text) # Removing '#' hash tag
 text = re.sub('RT[\s]+', '', text) # Removing RT
 text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
 
 return text


 df['Tweets'] = df['Tweets'].apply(cleanTxt)

 def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity


# Create two new columns 'Subjectivity' & 'Polarity'
st.df['Subjectivity'] = st.df['Tweets'].apply(getSubjectivity)
st.df['Polarity'] = st.df['Tweets'].apply(getPolarity)

# Show the new dataframe with columns 'Subjectivity' & 'Polarity'


allWords = ' '.join([twts for twts in df['Tweets']])
wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(allWords)


plt.imshow(wordCloud, interpolation="bilinear")
plt.axis('off')
plt.show()


def getAnalysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'
    
st.df['Analysis'] = st.df['Polarity'].apply(getAnalysis)



plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
st.df['Analysis'].value_counts().plot(kind = 'bar')
plt.show()



