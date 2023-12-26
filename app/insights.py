import pandas as pd
import plotly.express as px

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