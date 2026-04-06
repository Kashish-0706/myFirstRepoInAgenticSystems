import streamlit as st
import plotly.express as px
from fetch_data import get_cleaned_data, get_posts_per_user

# Set Page title
st.set_page_config(page_title="Data Dashboard", layout="wide")
st.title("Post Data Analysis Dashboard")

# Fetch data
data = get_cleaned_data()
user_counts = get_posts_per_user(data)

# Dtaset preview
st.header("Dataset Preview")
st.write(data.head(10))

# Posts per user (Bar Chart)
st.header("Number of Posts per User")
fig_bar = px.bar(user_counts, x="user_id", y="post_count", labels={"user_id": "User ID", "post_count": "Number of Posts"})
st.plotly_chart(fig_bar)

# Post length distribution (Histogram)
st.header("Distribution of Post Lengths")   
fig_hist = px.histogram(data, x="post_length", nbins=20, labels={"post_length": "Post Length"})
st.plotly_chart(fig_hist)