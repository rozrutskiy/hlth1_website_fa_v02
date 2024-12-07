import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get('client-id')
CLIENT_SECRET = os.environ.get('client-secret')

if CLIENT_ID is None or CLIENT_SECRET is None:
    raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in the environment variables")
