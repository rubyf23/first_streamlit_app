import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('BreakFast Menu')
streamlit.text('🥣 , Soup')
streamlit.text('🥣 , Soup')
streamlit.text('🥣 , Soup')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
