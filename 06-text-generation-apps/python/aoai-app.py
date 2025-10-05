# pylint: disable=all
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure Azure OpenAI service client 
client = AzureOpenAI(
    azure_endpoint = os.environ["AZURE_OPENAI_GPT4o_API_BASE"], 
    api_key=os.environ['AZURE_OPENAI_GPT4o_API_KEY'],  
    api_version = "2024-02-01"  # Updated API version
)

deployment=os.environ['AZURE_OPENAI_GPT4o_DEPLOYMENT']

# Let's verify the environment variables are loaded
print(f"Endpoint: {os.environ.get('AZURE_OPENAI_GPT4o_API_BASE')}")
print(f"Deployment: {deployment}")

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  

# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.99, max_tokens=100) #the lower the temperature, the more deterministic the output

# print response
print(completion.choices[0].message.content)