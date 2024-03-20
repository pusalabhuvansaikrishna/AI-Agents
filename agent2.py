import streamlit as st
from streamlit_option_menu import option_menu
option_menu(
  menu_title=None,
  options=['Agent1', "Agent2", "Agent3"],
  icons=['1-square-fill','2-square-fill','3-square-fill'],
  default_index=1,
  orientation="horizontal",)


st.session_state['role2']=st.text_input("Agent Role")
col1,col2 =st.columns(2)
with col1:
  st.session_state['goal2']=st.text_area("Goal")
with col2:
  st.session_state['backstory2']=st.text_area("Backstory")

st.session_state['description2']=st.text_area("Task Description")
st.session_state['output2']=st.text_area("Expcetd Output from the Agent")
  
col1, col2, col3, col4,col5=st.columns(5)
with col5:
  if(st.button("Next")):
    st.switch_page("pages/agent3.py")


