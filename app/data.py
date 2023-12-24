import streamlit as st
from datasets import load_dataset
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

hf_token = st.secrets['HF_TOKEN']

business_data_path = "yashraizada/yelp-open-dataset-top-businesses"
reviews_data_path = "yashraizada/yelp-open-dataset-top-reviews"
top_reviews_path = "yashraizada/top-reviews-per-business"
users_data_path = "yashraizada/yelp-open-dataset-top-users"

@st.cache_data
def get_business_data(path: str = business_data_path, train_split: int = 100) -> pd.DataFrame:
    return pd.DataFrame(load_dataset(path, split=f"train[:{train_split}%]", token=hf_token))

@st.cache_data
def get_reviews_data(path: str = reviews_data_path, train_split: int = 100) -> pd.DataFrame:
    return pd.DataFrame(load_dataset(path, split=f"train[:{train_split}%]", token=hf_token))

@st.cache_data
def get_top_reviews_per_business(path: str = top_reviews_path, train_split: int = 100) -> pd.DataFrame:
    return pd.DataFrame(load_dataset(path, split=f"train[:{train_split}%]", token=hf_token))

@st.cache_data
def get_users_data(path: str = users_data_path, train_split: int = 100) -> pd.DataFrame:
    return pd.DataFrame(load_dataset(path, split=f"train[:{train_split}%]", token=hf_token))

@st.cache_data
def get_business_names(business_dataset: pd.DataFrame) -> list:
    return business_dataset.name.unique()

@st.cache_data
def get_business_locations(business_dataset: pd.DataFrame, business_name: str) -> list:
    return business_dataset[business_dataset.name == business_name].address.unique()

@st.cache_data
def get_selected_business_reviews(reviews_dataset: pd.DataFrame, business_id: str) -> pd.DataFrame:
    return reviews_dataset[reviews_dataset.business_id == business_id].reset_index(drop=True)

@st.cache_data
def get_business_info(business_dataset: pd.DataFrame, business_name:str, business_address:str) -> dict:
    selected_business_dict = {}
    
    selected_business_id = business_dataset[(business_dataset.name == business_name) & (business_dataset.address == business_address)].reset_index().business_id[0]
    selected_business_dict['id'] = selected_business_id
    
    selected_business_dict['name'] = business_dataset[business_dataset.business_id == selected_business_id].name.item()
    selected_business_dict['city'] = business_dataset[business_dataset.business_id == selected_business_id].city.item()
    selected_business_dict['state'] = business_dataset[business_dataset.business_id == selected_business_id].state.item()
    selected_business_dict['postal_code'] = business_dataset[business_dataset.business_id == selected_business_id].postal_code.item()
    selected_business_dict['address'] = business_dataset[business_dataset.business_id == selected_business_id].address.item()
    selected_business_dict['categories'] = business_dataset[business_dataset.business_id == selected_business_id].categories.item()
    selected_business_dict['stars'] = business_dataset[business_dataset.business_id == selected_business_id].stars.item()
    
    selected_business_dict['price_range'] = '$' * int(business_dataset[business_dataset.business_id == selected_business_id].price_range.item())
    selected_business_dict['wifi'] = business_dataset[business_dataset.business_id == selected_business_id].wifi.item()
    selected_business_dict['appointment'] = business_dataset[business_dataset.business_id == selected_business_id].appointment.item()
    selected_business_dict['delivery'] = business_dataset[business_dataset.business_id == selected_business_id].delivery.item()
    
    selected_business_dict['review_count'] = business_dataset[business_dataset.business_id == selected_business_id].review_count.item()
    
    selected_business_dict['num_sentiment_0'] = business_dataset[business_dataset.business_id == selected_business_id].num_sentiment_0.item()
    selected_business_dict['num_sentiment_1'] = business_dataset[business_dataset.business_id == selected_business_id].num_sentiment_1.item()
    
    selected_business_dict['num_star_1'] = business_dataset[business_dataset.business_id == selected_business_id].num_star_1.item()
    selected_business_dict['num_star_2'] = business_dataset[business_dataset.business_id == selected_business_id].num_star_2.item()
    selected_business_dict['num_star_3'] = business_dataset[business_dataset.business_id == selected_business_id].num_star_3.item()
    selected_business_dict['num_star_4'] = business_dataset[business_dataset.business_id == selected_business_id].num_star_4.item()
    selected_business_dict['num_star_5'] = business_dataset[business_dataset.business_id == selected_business_id].num_star_5.item()
    
    return selected_business_dict

@st.cache_data
def get_user_info(user_dataset: pd.DataFrame, user_id: str) -> dict:
    selected_user_dict = {}
    
    selected_user_dict['id'] = user_id
    
    selected_user_dict['name'] = user_dataset[user_dataset.user_id == user_id].name.item()
    selected_user_dict['review_count'] = user_dataset[user_dataset.user_id == user_id].review_count.item()
    selected_user_dict['average_stars'] = user_dataset[user_dataset.user_id == user_id].average_stars.item()
    
    selected_user_dict['fans'] = user_dataset[user_dataset.user_id == user_id].fans.item()
    selected_user_dict['friends_count'] = user_dataset[user_dataset.user_id == user_id].friends_count.item()
    selected_user_dict['total_interactions'] = user_dataset[user_dataset.user_id == user_id].total_interactions.item()
    selected_user_dict['total_compliments'] = user_dataset[user_dataset.user_id == user_id].total_compliments.item()
    
    selected_user_dict['elite_years_count'] = user_dataset[user_dataset.user_id == user_id].elite_years_count.item()
    selected_user_dict['yelping_since'] = str(pd.to_datetime(user_dataset[user_dataset.user_id == user_id].yelping_since.item()).date())
    
    selected_user_dict['years_on_yelp'] = relativedelta(datetime.date.today(), user_dataset[user_dataset.user_id == user_id].yelping_since.item()).years
    
    return selected_user_dict