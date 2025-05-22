import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

path = get("C:\\stream\\a.json.json")
st_lottie(path)

def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
#url = get_url("") 
#st_lottie(url) 