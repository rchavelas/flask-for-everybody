from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Assign python variables to environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
