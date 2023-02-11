import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit.components.v1 as components

st.title("Hi, I'm Anzar")

st.write("Software Engineer | Self Taught Data Analyst |  Google Certified Data Analyst with expertise  in Data Analysis languages like R and Python, tools like Tableau, Big Query and fundamental concepts of Statistics. | I Love Data Viz")
st.write("")
############################## HTML ####################################

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
   <!DOCTYPE html>
<html>
  <head>
    <style>
      .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: white;
      }
      .navbar a {
        color: #333;
        text-decoration: none;
        font-weight: bold;
        margin-right: 20px;
      }
      
      .navbar::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 1px;
        background-color: #ddd;
      }
    </style>
  </head>
  <body>
    <nav class="navbar">
      <a href="https://github.com/anzarwani" target="_blank">Github</a>
      <a href="https://www.kaggle.com/anzarwani2" target="_blank">Kaggle</a>
      <a href="https://leetcode.com/user8201O/" target="_blank">Leetcode</a>
    </nav>
  </body>
</html>

    """,
    height=80,
)

######################### HTML ##############################



st.write("")
data_ed = {'Education':['Bachelors in Electronics and Communication', 'Google Data Analytics Certfication'],
           'Year': [2020, 2022]}

st.subheader("Education")

fig = px.bar(data_ed, y='Year', x='Education')
fig.update_traces(width=0.2)
fig.update_yaxes(range=[2015,2025]) 
st.plotly_chart(fig, use_container_width=True)

st.subheader("Projects")

expander1 = st.expander("Cyclistic - Google Data Analytics  Capstone Project (R).")
expander1.write("How Does a Bike-Share Navigate Speedy Success?")
expander1.image("cycle.png", width=200)
expander1.markdown("""<a href="https://www.kaggle.com/code/anzarwani2/cyclistic-google-data-analysis-capstone-project">Link to the Project</a>""", unsafe_allow_html=True)

expander2 = st.expander("Amazon Top 50 Bestselling Books - Data Viz (R).")
expander2.write("Fiction vs Non Fiction")
expander2.image("book.png", width=200)
expander2.markdown("""<a href="https://www.kaggle.com/code/anzarwani2/analysis-based-on-genre-of-books-r">Link to the Project</a>""", unsafe_allow_html=True)

expander3 = st.expander("Netflix EDA Dashboard (Python, Streamlit).")
expander3.write("Netflix Explanatory Data Analysis")
expander3.image("netflix.png", width=200)
expander3.markdown("""<a href="https://netflix-eda.up.railway.app/">Link to the Project</a>""", unsafe_allow_html=True)

expander4 = st.expander("Insurance Claim EDA (R).")
expander4.write("How does amount of insurance claim vary by gender, smokers, diabetics and the geographical region?")
expander4.write("Is there a correlation between health factors such as BMI, Blood Pressure and age?")
expander4.image("claim.png", width=200)
expander4.markdown("""<a href="https://www.kaggle.com/code/anzarwani2/insurance-claim-eda-in-r/">Link to the Project</a>""", unsafe_allow_html=True)

st.write("")
st.subheader("Certifications")

tab1, tab2, tab3, tab4 = st.tabs(["Google Data Analytics", "SQL for Data Science - UC DAVIS", "Data Analysis with Python - freecodecamp", "Python for Data Science - IBM"])

with tab1:
   st.image("https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~QMGNDZ8ZD6XQ/CERTIFICATE_LANDING_PAGE~QMGNDZ8ZD6XQ.jpeg", width=800)

with tab2:
   st.image("https://s3.amazonaws.com/coursera_assets/meta_images/generated/CERTIFICATE_LANDING_PAGE/CERTIFICATE_LANDING_PAGE~QFXEET6UJ2YU/CERTIFICATE_LANDING_PAGE~QFXEET6UJ2YU.jpeg", width=800)

with tab3:
   st.image("code.png", width=800)

with tab4:
   st.image("ibm.png", width=800)

st.subheader("Skills")
st.markdown("**Programming Languages**")
st.write("Python")
st.progress(100)
st.write("SQL")
st.progress(75)
st.write("R")
st.progress(50)

st.markdown("**Frameworks**")

python_code = '''import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt'''
st.code(python_code, language='python')

r_code = '''library(tidyverse)
library(ggplot)'''
st.code(r_code, language='r')

df_tools = pd.DataFrame({'Tools': ['Git', 'Spreadsheets', 'Tableau', 'MySQL', 'BigQuery', 'Jira'],
                         'Values': [1,1,1,1,1,1]})

st.markdown("**Tools**")
fig_tools = px.bar(df_tools, x='Values', y='Tools', color='Tools', height=400)
st.plotly_chart(fig_tools, use_container_width=True)



