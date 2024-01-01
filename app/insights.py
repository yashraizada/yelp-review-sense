import pandas as pd
import plotly.express as px

def plot_star_distribution_chart(business_dataset, business_id):
    stars = [5, 4, 3, 2, 1]
    stars_counts = [business_dataset[business_dataset.business_id == business_id][f"num_star_{i}"].item() for i in stars]

    chart_data = pd.DataFrame({'Stars': stars,
                               'Count': stars_counts})

    fig = px.bar(chart_data, x='Count', y='Stars',
             orientation='h',
             title=f'User Star Ratings',
             labels={'Count': 'Number of Ratings', 'Stars': 'Rating'})

    return fig

def plot_sentiment_chart(business_dataset, business_id, hole_size=0.6):
    negative_sentiment_count = business_dataset[business_dataset.business_id == business_id].num_sentiment_0.item()
    positive_sentiment_count = business_dataset[business_dataset.business_id == business_id].num_sentiment_1.item()

    chart_data = pd.DataFrame({'Sentiment': ['Positive', 'Negative'],
                               'Count': [positive_sentiment_count, negative_sentiment_count]})

    fig = px.pie(chart_data, values='Count', names='Sentiment', hole=hole_size,
                 title=f'Sentiment Distribution',
                 labels={'Count': 'Sentiment Count'})

    fig.update_traces(textinfo="percent+label", pull=[0, 0.1], showlegend=False)

    return fig

def plot_aspect_distribution_chart(business_dataset, business_id):
    aspects = ['clean', 'food', 'time', 'staff', 'location', 'service']
    aspects_counts = [business_dataset[business_dataset.business_id == business_id][f"abs_{aspect}_rating"].item() for aspect in aspects]

    chart_data = pd.DataFrame({'Aspects': aspects,
                               'Count': aspects_counts})

    fig = px.bar(chart_data, x='Count', y='Aspects',
             orientation='h',
             title=f'Aspect-based Ratings',
             labels={'Count': 'Average Rating', 'Aspects': 'Aspects'})
    
    fig.update_xaxes(range=(0, 5), tickvals=[0, 1, 2, 3, 4, 5])

    return fig