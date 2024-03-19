import pandas as pd
from urllib.parse import urlparse

# Function to get post id from url
def get_post_id(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Split the path components
    path_components = parsed_url.path.split('/')

    # Return fourth path element
    if len(path_components) < 5:
        raise ValueError("URL does not have enough path components.")
    return path_components[4]

# Function to scrape comments into dataframe, given a reddit instance and post url
def get_comments(reddit, post_id):
    # Create submission object
    submission = reddit.submission(post_id)

    #create empty list
    comments_list = []

    # Loop through comment objects and append attributes to list
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments_list.append([comment.score, comment.author, comment.body])
    
    # Convert list to dataframe
    df = pd.DataFrame(comments_list)
    
    # Rename columns
    df.columns = ['score', 'author', 'content']
    return df

