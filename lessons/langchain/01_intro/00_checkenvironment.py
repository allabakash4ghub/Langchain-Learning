import os
from dotenv import load_dotenv

# Load variables from the .env file

load_dotenv()

def checkenv(variable_name):
    if os.getenv(variable_name):
        print(f"✅ {variable_name}: Found")
    else:
        print(f"❌ {variable_name}: Not Found")

print("\nChecking the environment variables")        

checkenv("OPENAI_API_KEY")
checkenv("GROQ_API_KEY")
checkenv("GEMINI_API_KEY")
checkenv("LANGSMITH_API_KEY")
checkenv("HUGGINGFACEHUB_API_TOKEN")
