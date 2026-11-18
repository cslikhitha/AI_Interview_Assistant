import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice", page_icon = '💞', layout="centered")
st.title('AI Placement Assistent')
st.caption("Practice and prepare for your Placements here")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEYS"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title',['Machine Learning Engineer','Senior software engineer','Prompt Engineering','Data Analyst','Devop Engineer','other'])
if role == "other":
  st.text_input("Enter your Job Title","XXXXXXX")
model = st.selectbox("Model",['openai/gpt-oss-120b','openai/gpt-oss-20b'])
level = st.selectbox("Level",['Beginner','Intermediate','Advance'])
mode = st.radio("Activity",['Generate questions','Generate Coding Questions','Evaluate Answer','Improve Answer'])
if mode = 'Generate Questions':
   count = st.slider(1,10,5)
