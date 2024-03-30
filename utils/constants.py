import configparser
import os

# Get the absolute path of the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, '../config/config.conf')

parser = configparser.ConfigParser()
try:
    parser.read(config_file_path)

    # Retrieve values from the config file
    SECRET = parser.get('api_keys', 'reddit_secret_key')
    CLIENT_ID = parser.get('api_keys', 'reddit_client_id')
    DATABASE_HOST = parser.get('database', 'database_host')
    DATABASE_NAME = parser.get('database', 'database_name')
    DATABASE_PORT = parser.get('database', 'database_port')
    DATABASE_USER = parser.get('database', 'database_username')
    DATABASE_PASSWORD = parser.get('database', 'database_password')
    INPUT_PATH = parser.get('file_paths', 'input_path')
    OUTPUT_PATH = parser.get('file_paths', 'output_path')
    AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
    AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
    AWS_REGION = parser.get('aws', 'aws_region')
    AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')
    POST_FIELDS = (
        'id',
        'title',
        'score',
        'num_comments',
        'author',
        'created_utc',
        'url',
        'over_18',
        'edited',
        'spoiler',
        'stickied'
    )
    
    # Debugging: Print out retrieved values
    print("SECRET:", SECRET)
    print("CLIENT_ID:", CLIENT_ID)
    # Repeat for other variables...

except Exception as e:
    # Error handling
    print("Error reading config file:", e)
