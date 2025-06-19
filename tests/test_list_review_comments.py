# tests/test_list_review_comments.py
import pytest
from tests.conftest import client

def test_list_review_comments_default(client):
    resp = client["list"]()
    assert resp.status_code == 200
    # 返回一个列表
    assert isinstance(resp.json(), list)

def test_list_review_comments_pagination_empty(client):
    resp = client["list"](page=100, per_page=10)
    assert resp.status_code == 200
    # 超出页数，列表应为空
    assert resp.json() == []
