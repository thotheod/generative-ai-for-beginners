# pylint: disable=all
from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()


# configure Azure OpenAI service client 
client = OpenAI(
    base_url = os.environ["AZURE_MAI-DS-R1_API_BASE"], 
    api_key=os.environ['AZURE_MAI-DS-R1_API_KEY']
)

deployment=os.environ['AZURE_MAI-DS-R1_DEPLOYMENT']

# Let's verify the environment variables are loaded
print(f"Endpoint: {os.environ.get('AZURE_MAI-DS-R1_API_BASE')}")
print(f"Deployment: {deployment}")

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  

# make completion
completion = client.chat.completions.create(model=deployment, messages=messages) 

# print response
print(completion.choices[0].message.content)