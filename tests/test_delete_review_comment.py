# tests/test_delete_review_comment.py
import pytest
from tests.conftest import client, VALID_COMMENT_ID, INVALID_COMMENT_ID

@pytest.mark.skipif(VALID_COMMENT_ID == 0, reason="请设置 VALID_COMMENT_ID 环境变量")
def test_delete_review_comment_success(client):
    resp = client["delete"](VALID_COMMENT_ID)
    assert resp.status_code == 204

def test_delete_review_comment_not_found(client):
    resp = client["delete"](INVALID_COMMENT_ID)
    assert resp.status_code == 404

