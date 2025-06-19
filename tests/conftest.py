import pytest
from src.github_client import (
    list_review_comments,
    get_review_comment,
    delete_review_comment,
    update_review_comment,
    create_reply,
)

@pytest.fixture
def client():
    return {
        "list":     list_review_comments,
        "get":      get_review_comment,
        "delete":   delete_review_comment,
        "update":   update_review_comment,
        "reply":    create_reply,
    }
