# tests/test_create_reply.py
import pytest
from tests.conftest import client, VALID_COMMENT_ID, INVALID_COMMENT_ID

@pytest.mark.skipif(VALID_COMMENT_ID == 0, reason="请设置 VALID_COMMENT_ID 环境变量")
def test_create_reply_success(client):
    reply_body = "感谢你的建议！"
    resp = client["reply"](VALID_COMMENT_ID, reply_body)
    assert resp.status_code == 201
    data = resp.json()
    # 确认返回字段
    assert data["body"] == reply_body
    assert data.get("in_reply_to_id") == VALID_COMMENT_ID

def test_create_reply_not_found(client):
    resp = client["reply"](INVALID_COMMENT_ID, "任意")
    assert resp.status_code == 404
