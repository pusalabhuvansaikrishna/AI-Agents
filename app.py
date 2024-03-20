import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="AI Agents", page_icon="🧠",initial_sidebar_state="collapsed")

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

st.title("AI Agents and Conversation System")

with st.container(border=True):
  col1, col2=st.columns(2)
  with col1:
    st.image("/content/agents.jpeg",use_column_width=True)
  with col2:
    typewriter("The development of artificial intelligence (AI) agents represents a significant technological advancement, characterized by autonomous software programs capable of executing diverse tasks with human-like intelligence. This study is dedicated to investigating the creation of AI agents that integrate state-of-the-art capabilities for decision-making and natural language interaction. By drawing on the fundamental concepts of AI agents, this project endeavors to enhance their functionality by seamlessly incorporating real-time Internet data into decision-making processes and implementing contextually aware conversation systems.", 10)


st.markdown("---")

st.subheader("Experience the Magic of AI Agents, by clicking here ✨")
col1, col2, col3=st.columns(3)
with col2:
  if(st.button("Start Agents 🚀",use_container_width=True,type="primary")):
    bar = st.progress(50)
    time.sleep(1)
    bar.progress(100)
    st.switch_page("pages/agent1.py")


st.markdown("---")

st.subheader("⚙️ Tools Information")
data={
  "Tool":['Google Scrapper','ArXiv API','Exa','DuckDuckGo','Reddit'],
  "Description":["""A tool designed to extract relevant data from Google search results, 
  allowing users to programmatically access search results, snippets, and other information""",
  """An application programming interface (API) specifically tailored for accessing research papers and preprints from the arXiv repository. 
  Researchers and developers can use this API to retrieve scholarly articles related to specific topics""",
  """Exa is a specialized search engine that enables users to perform natural language queries and retrieve cleaned HTML content from desired documents. 
  It is particularly useful for learners and researchers seeking relevant information online.""",
  """DuckDuckGo is a privacy-focused search engine that provides search results without tracking user data. 
  It emphasizes user privacy and delivers relevant search results while avoiding personalized tracking.""",
  """Reddit is a popular online platform where users can participate in discussions, share content, and explore various topics through subreddits (specific interest-based communities). 
  The tool leverages Reddit’s vast user-generated content to provide insights and updates on specific subjects."""
  ],
}
df=pd.DataFrame(data)
st.table(df)


st.markdown("---")

with st.container(border=True):
  st.header("🦾 Team Details")
  col1,col2,col3=st.columns(3)
  with col1:
    st.image("/content/Bhuvan_Pic.jpeg",caption="Pusala Bhuvan Sai Krishna",use_column_width=True)
  with col2:
    st.image("/content/Bhavya_Pic.jpeg",caption='Kanumuri Bhavya Sri')
  with col3:
    st.image("/content/Pranay_Pic.jpeg",caption="Gali Pranay Reddy")

st.markdown("---")