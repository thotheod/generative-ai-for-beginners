from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the GITHUB_TOKEN variable
test_var = os.getenv("GITHUB_TOKEN")
print(f"The value is: {test_var}")