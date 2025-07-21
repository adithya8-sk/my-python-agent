from livekit import api
import os
from dotenv import load_dotenv

load_dotenv()

# Read your keys from .env
api_key = os.getenv("LIVEKIT_API_KEY")
api_secret = os.getenv("LIVEKIT_API_SECRET")

identity = "user123"          # Unique user identity
room_name = "jarvis-room"     # Room your assistant joins

# Create token object
token = api.AccessToken(api_key, api_secret)
token = token.with_identity(identity)
token = token.with_grants(
    api.VideoGrants(room_join=True, room=room_name)
)

# Print the JWT token
print("Generated Token:\n")
print(token.to_jwt())