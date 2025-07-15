import praw
from typing import List, Dict


def fetch_user_content(reddit: praw.Reddit, username: str, max_items: int = 100) -> List[Dict]:
    """
    Fetches the latest posts and comments from a Reddit user.
    Returns a list of dicts with type ('post' or 'comment'), content, and permalink.
    """
    user = reddit.redditor(username)
    items = []
    # Fetch submissions (posts)
    for submission in user.submissions.new(limit=max_items):
        items.append({
            'type': 'post',
            'content': submission.title + '\n' + submission.selftext,
            'permalink': f"https://www.reddit.com{submission.permalink}"
        })
    # Fetch comments
    for comment in user.comments.new(limit=max_items):
        items.append({
            'type': 'comment',
            'content': comment.body,
            'permalink': f"https://www.reddit.com{comment.permalink}"
        })
    return items 