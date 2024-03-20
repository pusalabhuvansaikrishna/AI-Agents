import streamlit as st
import os
import praw
from crewai import Agent, Task, Process, Crew
from langchain_openai import ChatOpenAI
from langchain.agents import Tool

os.environ['OPENAI_API_KEY']='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'
os.environ['OPENAI_MODEL_NAME']='gpt-3.5-turbo-0125'
os.environ['SERPER_API_KEY']='e37cb89dc694952c44c036c50cb62044acd70c2c'
os.environ['EXA_API_KEY'] ='bab3594a-7620-42f7-9b20-63b0b0a9cd2f'

#Google Scrapper
from langchain.utilities import GoogleSerperAPIWrapper
search=GoogleSerperAPIWrapper()
search_tool=Tool(
    name="Google Scraper Tool",
    func=search.run,
    description='use this tool when you want to explore latest or real-time information from internet(This is from google search engine)',
)

#ArXiv Research Tools
from langchain_community.utilities import ArxivAPIWrapper
arxiv = ArxivAPIWrapper()
research_paper_tool=Tool(
    name="Arxiv Research Tool",
    func=arxiv.run,
    description='use this tool when the decision need the scientific evidence and latest research on a topic with the help of a keyword, that best describes the problem about!',
)

#Exa Tools
from exa_py import Exa
from langchain.agents import tool

exa = Exa(api_key=os.environ["EXA_API_KEY"])

@tool
def search_exa(query: str):
    """Search for a webpage based on the query."""
    return exa.search(f"{query}", use_autoprompt=True, num_results=5)

exa_search=Tool(
    name="Exa Webpage Search",
    func=search_exa.run,
    description="use this tool, when you need a webpages on a particular topic",
)

@tool
def find_similar_exa(url: str):
    """Search for webpages similar to a given URL.
    The url passed in should be a URL returned from `search_exa`.
    """
    return exa.find_similar(url, num_results=5)

exa_similar_search=Tool(
    name='Exa Similar Webpages',
    func=find_similar_exa.run,
    description="you have a url and you need other websites that share the similarity in content with the given url, then use this tool",
)

#Duck Duck Go
from langchain.tools import DuckDuckGoSearchResults
duck_search = DuckDuckGoSearchResults()
duck_search_tool=Tool(
    name="Duck Duck go",
    func=duck_search.run,
    description="use this tool when you want to explore latest or real-time information from internet, in this results are not baised",
)


#reddit

from langchain.tools import tool
import time
class BrowserTool:
  @tool("scrape reddit content")
  def scrape_reddit(subredd:str,max_comment_per_post=7):
    """Useful to scrape a reddit content, you pass the keyword as a paramater to this function that keywods defines on which topic you want to search reddit"""
    reddit=praw.Reddit(
        client_id="YkR1zPiNwyMeNIDuRbThew",
        client_secret="3bx2-DLZWUJ-IUP4EsKhL_vcb_F0Pw",
        user_agent="my-app by u/Cool_Awareness3587",
        check_for_async=False,
    )
    subreddit=reddit.subreddit(subredd)
    scrapped_data=[]

    for post in subreddit.hot(limit=12):
      post_data={"title":post.title, "url":post.url, "comments":[]}
      try:
        post.comments.replace_more(limit=0)
        comments=post.comments.list()
        if max_comment_per_post is not None:
          comments=comments[:7]

        for comment in comments:
          post_data["comments"].append(comment.body)

        scrapped_data.append(post_data)
      except praw.exceptions.APIException as e:
        print(f"API Exceptions: {e}")
        time.sleep(60)
    return scrapped_data


#Agents Creation
ag1=Agent(
    role=st.session_state['role1'],
    goal=st.session_state['goal1'],
    backstory=st.session_state['backstory1'],
    verbose=True,
    allow_delegation=True,
    tools=[search_tool,research_paper_tool,duck_search_tool, exa_search, exa_similar_search,BrowserTool().scrape_reddit],
    memory=True,)


ag2= Agent(
    role=st.session_state['role2'],
    goal=st.session_state['goal2'],
    backstory=st.session_state['backstory2'],
    verbose=True,
    allow_delegation=True,
    tools=[search_tool,research_paper_tool,duck_search_tool, exa_search, exa_similar_search,BrowserTool().scrape_reddit],
    memory=True,)

ag3=Agent(
    role=st.session_state['role3'],
    goal=st.session_state['goal3'],
    backstory=st.session_state['backstory3'],
    verbose=True,
    allow_delegation=True,
    tools=[search_tool,research_paper_tool,duck_search_tool, exa_search, exa_similar_search,BrowserTool().scrape_reddit],
    memory=True,)


# Task Assignment
task1 = Task(
    description=st.session_state['description1'],
    expected_output=st.session_state['output1'],
    agent=ag1,)

task2 = Task(
    description=st.session_state['description2'],
    expected_output=st.session_state['output2'],
    agent=ag2,)

task3= Task(
    description=st.session_state['description3'],
    expected_output=st.session_state['output3'],
    agent=ag3,)


crew = Crew(
    agents=[ag1, ag2, ag3],
    tasks=[task1, task2, task3],
    verbose=2,
    manager_llm=ChatOpenAI(temperature=0.2,model='gpt-3.5-turbo'),
    process=Process.hierarchical,
)

with st.spinner(text="In progress"):
  result=crew.kickoff()
  st.success("Done")

st.code(result)
st.balloons()