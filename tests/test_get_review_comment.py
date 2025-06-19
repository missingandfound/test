import pytest

@pytest.mark.parametrize("comment_id, expected_status", [
    (42,      200),   # 有效 comment_id
    (99999,   404),   # 不存在
])
def test_get_review_comment(client, comment_id, expected_status):
    resp = client["get"](comment_id)
    assert resp.status_code == expected_status
