import numpy as np
import streamlit as st

def set_page_config():
    return st.set_page_config(
        page_title="Yelp Review Sense",
        page_icon=":yelp:",
        layout="wide", 
        menu_items={ 
            'Get Help': "https://github.com/yashraizada/yelp-review-sense", 
            'Report a bug': "mailto:yash.raizada@hotmail.com", 
            'About': "Discover sentiment insights from Yelp reviews"
        }
    )
    
def draw_line():
    return st.divider()

def draw_space(size: int = 3):
    return st.markdown("#" * np.clip(size, 0, 6))