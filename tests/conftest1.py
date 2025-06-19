# tests/conftest.py
import os
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
        "list":   list_review_comments,
        "get":    get_review_comment,
        "delete": delete_review_comment,
        "update": update_review_comment,
        "reply":  create_reply,
    }

# 方便在测试里引用
VALID_COMMENT_ID = int(os.getenv("VALID_COMMENT_ID", "0"))
INVALID_COMMENT_ID = 999999999
