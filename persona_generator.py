import sys
import os
import praw
from urllib.parse import urlparse
from utils.reddit_scraper import fetch_user_content
from utils.llm_persona_builder import build_persona_with_llm
 
# --- Add your Reddit API credentials here ---
REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET_KEY"
REDDIT_USER_AGENT = "script:User_Name_Persona:v1.0 (by u/USER_NAME)"
# -------------------------------------------

def extract_username_from_url(url: str) -> str:
    """Extracts the Reddit username from a profile URL."""
    path = urlparse(url).path
    parts = [p for p in path.split('/') if p]
    if len(parts) >= 2 and parts[0] == 'user':
        return parts[1]
    raise ValueError("Invalid Reddit profile URL")


def main():
    if len(sys.argv) != 2:
        print("Usage: python persona_generator.py <reddit_profile_url>")
        sys.exit(1)
    profile_url = sys.argv[1]
    try:
        username = extract_username_from_url(profile_url)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Initialize Reddit API with credentials directly
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    print(f"Fetching posts and comments for user: {username}")
    user_content = fetch_user_content(reddit, username)
    if not user_content:
        print("No content found for this user.")
        sys.exit(1)

    print("Generating persona using LLM...")
    persona = build_persona_with_llm(user_content)

    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", f"{username}_persona.txt")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(persona)
    print(f"Persona saved to {output_path}")

if __name__ == "__main__":
    main() 