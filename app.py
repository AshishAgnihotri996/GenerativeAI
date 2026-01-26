import streamlit as st
#import this to use throught the app / project its obj and its methods
#creating any file name like app or any other is important to run this file by using cmd : streamlit run app.py

st.title("Helloo this is the first msg")
st.write("welcome to my first steamlit app")


#basic UI elements

st.title("title")
st.header("header")
st.subheader("Subheader")
st.text("simple text")
st.markdown("**Bold**,*Italic*")


#to take inputs from user
name = st.text_input("enter your name")
age = st.number_input("enter your age",min_value=0)

if st.button('Submit'):
    st.write(f"Hello{name},age{age}")


# select / checkbox / radio

language = st.selectbox("select your language",['python','java','c','c++'])
agree = st.checkbox('I agree')

choice =st.radio("Gender",['male','female'])


# to display data
# lets use pandas df to view

import pandas as pd

Df = pd.DataFrame(
    {
        "Name":['Ashish','Agnihotri'],
        "Score":[90,85]
    }
)
st.text("dynamic data frame | try using filters | dropdowns | drag and drop")
st.dataframe(Df) #dy
st.write("static table df")
st.table(Df)#st

#charts
import plotly
st.area_chart(Df)
st.bar_chart(Df)
# st.altair_chart(Df)
# st.graphviz_chart(Df)
# st.plotly_chart(Df)
# st.pydeck_chart(Df)
# st.vega_lite_chart(Df)

#layouts with columns | sidebars



st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Select page",
    ["Select", "Home", "Page", "About"]
)

if option == "Home":
    st.switch_page("pages/home.py")

elif option == "Page":
    st.switch_page("pages/page.py")

elif option == "About":
    st.switch_page("pages/about.py")



#Columns

col1,col2 = st.columns(2)

with col1:
    st.write("left column")
with col2:
    st.write("right column")


#session state

if "count" not in st.session_state:
    st.session_state.count =0

if st.button("increment"):
    st.session_state.count+=1

st.write("Count",st.session_state.count)


#file upload

file =st.file_uploader("Upload csv",type="csv")

if file:
    df=pd.read_csv(file)
    st.dataframe(df)