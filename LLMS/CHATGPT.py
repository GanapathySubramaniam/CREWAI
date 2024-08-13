import os
from langchain_openai import ChatOpenAI

chatgpt= ChatOpenAI(model='gpt-3.5-turbo',
                   verbose=True,
                   temperature=0.5,
                   openai_api_key=os.getenv('OPENAI_API_KEY'))
