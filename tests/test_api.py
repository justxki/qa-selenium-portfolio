import pytest
import requests
import json

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    response = requests.get(url)
    body = response.json()
    print(json.dumps(body, indent=2))
    assert response.status_code == 202
    assert 'Python' in body['AbstractText']