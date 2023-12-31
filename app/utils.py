import numpy as np
import streamlit as st
from datetime import datetime

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

def truncate_text(text: str, length: int = 100):
    if len(text) > length:
        return text[:length] + ' ...'
    
    return text

def print_date(timestamp: datetime):
    month = timestamp.strftime('%b')
    date = timestamp.strftime('%-d')
    year = timestamp.strftime('%Y')
    hour = timestamp.strftime('%I')
    minute = timestamp.strftime('%M')
    ampm = timestamp.strftime('%p')

    return f"{month} {date}, {year} at {hour}:{minute} {ampm}"