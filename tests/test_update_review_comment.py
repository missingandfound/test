# tests/test_update_review_comment.py
import pytest
from tests.conftest import client, VALID_COMMENT_ID, INVALID_COMMENT_ID

@pytest.mark.skipif(VALID_COMMENT_ID == 0, reason="请设置 VALID_COMMENT_ID 环境变量")
def test_update_review_comment_success(client):
    new_body = "这是更新后的评论内容"
    resp = client["update"](VALID_COMMENT_ID, new_body)
    assert resp.status_code == 200
    data = resp.json()
    assert data["body"] == new_body

def test_update_review_comment_not_found(client):
    resp = client["update"](INVALID_COMMENT_ID, "任意内容")
    assert resp.status_code == 404
