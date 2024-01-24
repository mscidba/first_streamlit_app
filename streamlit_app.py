#Created the main Python file
import streamlit
streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 and blueberry oatmeal')
streamlit.text('🥗 Kale, spinach and Rocket smoothie')
streamlit.text('🐔 Hard-boiled free-range egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlist.dataframe(my_fruit_list)
