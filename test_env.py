from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the AZURE_OPENAI_GPT4o_API_BASE variable
test_var = os.getenv("AZURE_OPENAI_GPT4o_API_BASE")
print(f"The value is: {test_var}")