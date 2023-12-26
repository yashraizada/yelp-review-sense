import streamlit as st

from data import * 
from utils import *
from images import *
from insights import *

# Setting Page Config
set_page_config()

# Load datasets
business_dataset = get_business_data()
top_reviews_dataset = get_top_reviews_per_business()
user_dataset = get_users_data()
business_names = get_business_names(business_dataset)

# Define Search Buttons
_, select_business_col, select_location_col, _ = st.columns([1, 1, 1, 1])

with select_business_col:
    selected_business = st.selectbox(label="Select a business", options=business_names, placeholder="Search for a business...", index=None, label_visibility="hidden")

with select_location_col:
    if selected_business:
        options = get_business_locations(business_dataset, selected_business)
        index_value = 0
    else:
        options = ["Select a business to see locations"]
        index_value = None
    
    selected_location = st.selectbox(label="Select a location", options=options, placeholder="in United States of America", index=index_value, label_visibility="hidden")

# Adding space after the search buttons
draw_space()
    
# Define columns for business info and review insights
business_info_col, _, review_insights_col = st.columns([0.6, 0.1, 0.3])

with business_info_col:
    # Define columns for business image, business description, and business review summary
    business_image_col, _, business_description_col, _, business_review_summary_col = st.columns([0.2, 0.05, 0.4, 0.05, 0.3])
    
    if selected_business:
        # Get a dictonary with all information for the selected business
        selected_business_dict = get_business_info(business_dataset, selected_business, selected_location)
        
        with st.container():
            with business_image_col:
                st.image(get_business_logo_url(selected_business_dict['name'].lower()))
    
            with business_description_col:
                st.subheader(selected_business_dict['name'])
                st.markdown(f'''{selected_business_dict['address']}  
                {selected_business_dict['price_range']}&nbsp;&nbsp;•&nbsp;&nbsp;{selected_business_dict['wifi']} Wifi&nbsp;&nbsp;•&nbsp;&nbsp;{selected_business_dict['categories']}
                ''')
    
            with business_review_summary_col:
                st.subheader("Overall Rating")
                st.image(get_business_stars_url(selected_business_dict['stars']), width=150)
                st.markdown(f"##### {selected_business_dict['review_count']} reviews")

        draw_space()
        draw_line()
        
        selected_business_reviews = get_selected_business_reviews(top_reviews_dataset, selected_business_dict['id'])

        st.subheader('Recommended Reviews')
        draw_space()

        for i in range(5):
            # Define columns for user avatar and user info
            user_avatar_col, user_info_col = st.columns([0.1, 0.9])

            # Load dependencies
            review_dict = selected_business_reviews.iloc[i, :]
            
            user_id = review_dict['user_id']
            user_info_dict = get_user_info(user_dataset, user_id)
            user_avatar_url = get_user_avatar_url(user_id)
        
            with st.container():
                with user_avatar_col:
                    st.image(user_avatar_url)
        
                with user_info_col:
                    st.markdown(f"###### {user_info_dict['name']}")
                    st.markdown(f"{user_info_dict['review_count']} reviews&nbsp;&nbsp;•&nbsp;&nbsp;{user_info_dict['fans']} fans&nbsp;&nbsp;•&nbsp;&nbsp;{user_info_dict['friends_count']} friends&nbsp;&nbsp;•&nbsp;&nbsp;{user_info_dict['years_on_yelp']} years on Yelp&nbsp;&nbsp;•&nbsp;&nbsp;Elite for {user_info_dict['elite_years_count']} years")
        
            with st.container():
                review_rating_col, review_date_col = st.columns([0.12, 0.88])

                with review_rating_col:
                    st.image(get_business_stars_url(review_dict['stars']))

                with review_date_col:
                    st.markdown(review_dict['date'])

            with st.container():
                st.markdown(review_dict['text'])

            draw_space()

with review_insights_col:
    if selected_business:
        rating = plot_star_distribution_chart(business_dataset, selected_business_dict['id'])
        st.plotly_chart(rating, use_container_width=True)
        
        sentiment = plot_sentiment_chart(business_dataset, selected_business_dict['id'])
        st.plotly_chart(sentiment, use_container_width=True)