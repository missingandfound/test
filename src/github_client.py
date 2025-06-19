import os, requests
from dotenv import load_dotenv

load_dotenv()

API_BASE = "https://api.github.com"
TOKEN    = os.getenv("GITHUB_TOKEN")
HEADERS  = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
OWNER = os.getenv("GITHUB_OWNER")
REPO  = os.getenv("GITHUB_REPO")

def list_review_comments(page=None, per_page=None):
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/pulls/comments"
    params = {}
    if page:      params["page"] = page
    if per_page:  params["per_page"] = per_page
    return requests.get(url, headers=HEADERS, params=params)

def get_review_comment(comment_id):
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/pulls/comments/{comment_id}"
    return requests.get(url, headers=HEADERS)

def delete_review_comment(comment_id):
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/pulls/comments/{comment_id}"
    return requests.delete(url, headers=HEADERS)

def update_review_comment(comment_id, body):
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/pulls/comments/{comment_id}"
    return requests.patch(url, headers=HEADERS, json={"body": body})

def create_reply(comment_id, body):
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/pulls/comments/{comment_id}/replies"
    return requests.post(url, headers=HEADERS, json={"body": body})
