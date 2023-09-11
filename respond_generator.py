import json
import openai
import os


def lambda_handler(event, context):
    # OpenAI credential
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    payload = json.loads(event['body'])
    tweet = payload['tweet']
    author = payload['author']

    def create_respond(tweet, author):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            n=5,
            messages=[
                {"role": "user", "content": f"Create a respond to @{author}'s tweet: '{tweet}'"}
            ]
        )
        return completion

    generate = create_respond(tweet, author)

    respond1 = generate['choices'][0].message.content
    respond2 = generate['choices'][1].message.content
    respond3 = generate['choices'][2].message.content
    respond4 = generate['choices'][3].message.content
    respond5 = generate['choices'][4].message.content

    return {
        'statusCode': 200,
        'body': json.dumps(
            f'Tweet by {author}: {tweet}\nResponds;\n{respond1}\n{respond2}\n{respond3}\n{respond4}\n{respond5}\n')
    }
