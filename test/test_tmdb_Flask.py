from unittest.mock import Mock
from main2 import app
import pytest


@pytest.mark.parametrize('n, result', (
    ('popular', 200),
    ('top_rated', 200),
    ('upcoming', 200),
    ('now_playing', 200)
))
def test_homepage(monkeypatch, n, result):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
