import tkinter as tk
import praw
from ..general import load_config
from ..scraper import get_post_id, get_comments
from wordcloud import create_wordcloud
from gui_utils import MultiInputDialog, get_output_filepath_from_dialog

def main():
    # Hide the root window
    root = tk.Tk()
    root.withdraw()

    # Request parameters from user
    dialog = MultiInputDialog(root, title='Enter parameters')
    paras = dialog.result

    # Raise error if missing all parameters
    if not paras:
        raise ValueError('Missing all required parameters')
    
    # Set up reddit instance
    config = load_config()
    client_id = config["client_id"]
    client_secret = config["client_secret"]

    reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password='',
    username='',
    user_agent='YOURUSERAGENT',
    check_for_async=False
    )

    # Get comments dataframe
    post_id = get_post_id(paras[0])
    comments_df = get_comments(reddit, post_id)

    # Request output location from user
    output_path = get_output_filepath_from_dialog('Create the output Excel file')

    # Create wordcloud
    create_wordcloud(df, r'images\arsenal_badge.png', paras[1], output_path, paras[2], paras[3]) # mask is hard coded for now 

    print('Done!')

if __name__ == '__main__':
    main()