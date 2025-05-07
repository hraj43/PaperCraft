import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Text Generation Settings
EMBEDDING_MODEL = "text-embedding-3-small"
GENERATION_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 1000

# Paper section settings
INTRODUCTION_MIN_WORDS = 300
INTRODUCTION_MAX_WORDS = 500

