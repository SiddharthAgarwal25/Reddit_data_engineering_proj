from etls.reddit_etl import connection_to_reddit, extract_posts, transform_data, load_data_to_csv
import pandas as pd
import praw
import sys
from pathlib import Path
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import OUTPUT_PATH, CLIENT_ID, SECRET
import pandas as pd
from praw import Reddit


def redit_pipeline(file_name,subreddit, time_filter, limit):
    instance = connection_to_reddit(CLIENT_ID, SECRET, 'FewTranslator233')
    posts = extract_posts(instance, subreddit, time_filter, limit)
    posts_data = pd.DataFrame(posts)
    post_data = transform_data(posts_data)
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_data, file_path)

    return file_path

