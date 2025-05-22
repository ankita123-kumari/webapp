from PIL import Image
import json
import requests 

import streamlit as st
from streamlit_lottie import st_lottie 

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load assets

lottie_coding =load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# ---- HEADER SECTION ----
# img_contact_form = Images.open("C:\20 project using html")


#with open("C:\\stream\\b.json", "r") as f:
    ##data = json.load(f)  # Load JSON properly
    #print(data)  # Print structured content
# img_lottie_animation =Image.open("C:\\stream\\a.json.json", "r")
with open("C:\\stream\\b.json", "r") as f:
    lottie_animation = json.load(f)
img_contact_form = Image.open("C:\stream/R.png","r")
with st.container():
    st.subheader("Hi, I am ankita :wave:")
    st.title("A Data Analyst From india")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient.")
    st.write("[Learn More >](https://pythonandvba.com)")

# what i do

with st.container():
    st.write("----")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("#")
        st.write(
            """
             On my YouTube channel I am creating tutorials for people who:
        - are looking for a way to leverage the power of Python in their day-to-day work.
        - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
        - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
        - are working with Excel and found themselves thinking - "there has to be a better way."

        If this sounds interesting to you, consider subscribing and turning on the notifications.
        """
               )

        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_animation, height = 300, key='coding')

# projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("###")  
    image_column, text_column = st.columns((1,2))

    with image_column:

        #insert image
        #st.image(img_lottie_animation)
     with text_column:
         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
         st.write(
             """
             Learn how to use Lottie Files in Streamlit!
             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it
             In this tutorial, I'll show you exactly how to do it
             """)

         st.markdown("[Watch Video...](http://youtu.be/TXSOitGoINE)")
with st.container():
    image_column,text_column= st.columns((1,2))
    with image_column:
        st.image(img_contact_form) 
    with text_column:
        st.subheader("How To ADd A Contact Form To Your Streamlite App") 
        st.write(
            """
            want to add a contact form to yoyr streamlit website?
            In this video,I'm going to show how to implement a contact form in your streamlite
            """

        )           
st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

# Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
<form action="https://formsubmit.co/codingisfun.testuser@gmail.com" method="POST">
    <input type="hidden" name="-captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:

    st.markdown(contact_form, unsafe_allow_html=True)

with right_column:
    st.empty()    