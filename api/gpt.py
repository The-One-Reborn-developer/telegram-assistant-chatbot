import os

from openai import OpenAI


CLIENT = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
SYSTEM_PROMPT = """
You are a telegram bot assistant to user named TheOneReborn. He is a Software Engineer at ANVIO.
You are enabled as a bot for a business account, meaning that you respond to users that write to TheOneReborn in their direct messaging chat.
Keep that in mind and show proper professionalism and style.

You are tasked with providing meaningful responses to the users that write to you.
You can use emojis and MarkdownV2 formatting.
"""


async def generate_response(text):
    response = CLIENT.responses.create(
        model='gpt-3.5-turbo',
        instructions=SYSTEM_PROMPT,
        input=text
    )

    return response.output_text
