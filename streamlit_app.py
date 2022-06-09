from operator import index
import streamlit
import pandas
FILENAME = "fruit_macros.txt"
LOCATION = "us-west-2"
DOMAIN = "uni-lab-files"
CLOUD = "amazonaws"
fruits_url = f"""https://{DOMAIN}.s3.{LOCATION}.{CLOUD}.com/dabw/{FILENAME}"""

streamlit.title('My Parents new Healthy Diner')
streamlit.header('breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Hard-BoiledAvocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = (pandas.read_csv(fruits_url)
                 .set_index("Fruit")
                 )
fruits_selected = (streamlit.multiselect("Pick some fruits:",
                   list(my_fruit_list.index),
                    ["Avocado", "Strawberries"])
                   )
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
