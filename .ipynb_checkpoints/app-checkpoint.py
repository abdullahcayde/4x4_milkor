# ------------------------------ Streamlit MyWebsite Project 02 ------------------------------
#Project_Date : 04.08.2022
#Project Purpose : Make a website with streamlit dictionary
#Project Process :
    #0 -  Install and Import Packages (streamlit, Pillow, streamlit_lottie)
    #1 - Set Page Configrations title, icon, layout
    #2 - Use Local Css to config. Website (create style directory)
    #3 - Load Assets (lottie, images) (Create images directory and put the images here)
    # 4 - Header Section01 
#background-image : url('http://www.military-today.com/apc/milkor_4x4.jpg')
#background-size : cover;
    # 5- What I do Section02
    
    
import pandas as pd
import numpy as np
import seaborn as sns
import os


import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# 1 - Set Page Configrations
st.set_page_config(page_title="Abdullah Cay", page_icon=":tada:", layout="wide")

# 3 - Load Assets (images)

img01 = Image.open('images/01.jpg')
img02 = Image.open('images/02.jpg')
img03 = Image.open('images/03.jpg')
img04 = Image.open('images/04.jpg')
img05 = Image.open('images/05.jpg')
img06 = Image.open('images/06.jpg')



# 2 - Use Local Css to config. Website

page_bg_img = '''
<style>
[data-testid = 'stAppViewContainer'] {
background-color: #fefbd1

}
<style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)




# 4 - Headers Section01
#st.subheader("Hi, I am Abdullah Cay :wave:")
st.title("4x4 Milkor Armoured Personnel Carier (APC) Project")
st.subheader(
        '''
        In this website you will see details about 4x4 Milkor Project
         - **Title** : 4x4 Milkor Armoured Personal Carier
         - **Purpose** : Prototype 4x4 APC Manufacturing
         - **Timeline** : 22.05.20217 - 18.09.2018
         - **Location** : South Africa / Johannesburg
         ''')



# 5- What I do Section02
st.write('---')
with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.header('What I did in this project ?')
        st.write('##')
        st.write(
            '''
            I worked as a Project Manager Assistant and Mechanical Engineer ;
            - Designing, specifying, prototyping, documenting, procuring, qualifying, implementing and improving equipment and its components for manufacturing and test.
            - Ballistic protection level tests and analysis.
            - 3D Modelling experience using Autodesk Inventor tools.
            - Production line management roles.
            - Communication/presentation of production/design results to internal stakeholders.
            ''')
        
# 6 - Projects
# 6.1 - Project01 - Pandas Visualization - Section03
with st.container():
    st.write('---')
    st.header('Our Truck IVECO250E14 came to the nest')
    st.write('##')
    image_column01 , image_column02, image_column03 = st.columns(3)

    with image_column01:
        st.image(img01)
        
    with image_column02:
        st.image(img02)
        
    with image_column03:
        st.image(img03)
        
# 6.2 - Project01 - Pandas Visualization - Section04
with st.container():
    st.write('---')
    st.header('Our Truck IVECO250E14 came to the nest')
    st.write('##')
    image_column01 , image_column02, image_column03 = st.columns(3)

    with image_column01:
        st.image(img04)
        
    with image_column02:
        st.image(img05)
        
    with image_column03:
        st.image(img06)