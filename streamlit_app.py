from operator import index
import streamlit
import pandas
fruit_list_remote = """https://uni-lab-files.s3.us-west-2.amazonaws.com
/dabw/fruit_macros.txt"""

streamlit.title('My Parents new Healthy Diner')
streamlit.header('breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Hard-BoiledAvocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = (pandas.read_csv(fruit_list_remote)
                 .set_index("Fruit")
                 )
streamlit.multiselect("Pick some fruits:" list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
