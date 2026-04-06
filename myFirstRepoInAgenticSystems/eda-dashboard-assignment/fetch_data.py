import pandas as pd
import requests

def get_cleaned_data():
    # Fetch post data from the API
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    # Convert JSON response into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Rename userId to user_id and drop the id column
    df = df.rename(columns={"userId": "user_id"})
    df = df.drop(columns=["id"])

    # Create a new column 'post_length'
    df["post_length"] = df["body"].apply(len)
    return df

def get_posts_per_user(df):
    # Count how many posts each user has made
    user_counts = df.groupby("user_id").size().reset_index(name="post_count")
    return user_counts

    