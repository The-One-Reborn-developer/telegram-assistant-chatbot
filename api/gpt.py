import os

from openai import OpenAI


CLIENT = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
SYSTEM_PROMPT = """
You are a helpful assistant. Provide the user with the necessary information.
"""


def generate_response(text):
    response = CLIENT.responses.create(
        model='gpt-3.5-turbo',
        instructions=SYSTEM_PROMPT,
        input=text
    )

    return response.output_text
