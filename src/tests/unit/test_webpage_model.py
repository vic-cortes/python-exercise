import pytest
import requests
import requests_mock

# from app.models.webpage import Webpage


@pytest.fixture(scope="module")
def mock_test_url(requests_mock):
    return requests_mock.get("http://test.com", text="data")


def test_request_data(mock_test_url):
    assert "data" == requests.get("http://test.com").text
