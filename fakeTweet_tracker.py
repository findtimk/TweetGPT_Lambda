import json
import openai
import random
import requests
import datetime
import pymysql
import os

# OpenAI & RDS MySQL Credentials
openai.api_key = os.environ.get('OPENAI_API_KEY')
endpoint = os.environ.get('DB_HOST')
database = os.environ.get('DB_NAME')
username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
port = os.environ.get('DB_PORT')

# Database Connection
conn = pymysql.connect(host=endpoint, user=username, password=password, port=int(port), database=database)

# API Gateway
endpoint = "https://wvm7ef0q3b.execute-api.eu-north-1.amazonaws.com/respondGenerator"
headers = {"Content-Type": "application/json"}


# Internal Functions
def create_tweet(name):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate random tweet like you're {name}."}
        ]
    )
    return completion


def add_tweet_data(your_name, tweet_id, tweet_sender, tweet_text, formatted_datetime):
    cursor = conn.cursor()
    cursor.execute("SELECT tweet_id FROM {}_data WHERE tweet_id = %s".format(your_name), (tweet_id,))
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO {}_data (tweet_id, tweet_sender, tweet_text, tweet_datetime) VALUES (%s, %s, %s, %s)".format(
                your_name), (tweet_id, tweet_sender, tweet_text, formatted_datetime))
        conn.commit()


"""
def get_tweets(your_name, username):
    global last_tweet_ids
    tweets = api.user_timeline(screen_name=username, exclude_replies=True, count=1, since_id=last_tweet_ids[username])
    if tweets:
        last_tweet_ids[username] = tweets[0].id
        for tweet in tweets:
            status = api.get_status(tweet.id)
            creation_date = status.created_at
            formatted_datetime = creation_date.strftime("%m-%d-%Y %I:%M %p")
            if "&amp;" in tweet.text:
                tweet.text = tweet.text.replace("&amp;", "&")
            add_tweet_data(your_name, tweet.id, username, tweet.text, formatted_datetime)
            print(f"{username}: - {tweet.text} // {tweet.id} at {formatted_datetime}")
"""


def get_tweets(name, author):
    generate = create_tweet(author)
    tweet_text = generate['choices'][0].message.content
    tweet_id = random.randint(100000000, 999999999)
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%m-%d-%Y %I:%M %p")
    # add_tweet_data(name, tweet_id, author, tweet_text, formatted_datetime)

    payload = {'tweet': tweet_text, 'author': author}
    payload_json = json.dumps(payload)
    response = requests.post(endpoint, data=payload_json, headers=headers)
    if response.status_code == 200:
        print("Request successful!")
        print("----------------------------------------------------------------------------------------------------")
        print("Response:", response.text)
        print("----------------------------------------------------------------------------------------------------")
    else:
        print("Request failed. Status code:", response.status_code)
        print("Response:", response.text)


# Main Handler Function
def lambda_handler(event, context):
    cursor = conn.cursor()

    tables = []
    _tracking_tables = []

    cursor.execute("SHOW TABLES;")
    tables_tuple = cursor.fetchall()

    for i in tables_tuple:
        tables.append(i[0])

    for table in tables:
        if table.endswith('_tracking'):
            _tracking_tables.append(table)

    for table in _tracking_tables:
        real_name = table[:-9]
        cursor.execute(f"SELECT username FROM {table};")
        usernames = cursor.fetchall()

        for username in usernames:
            get_tweets(real_name, username[0])
