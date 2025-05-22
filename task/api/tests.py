from unittest.mock import patch
import pytest
from api.load_users import get_users_from_api
from api.models import User


MOCKED_API_RESPONSE = {
    "results": [
        {
            "gender": "female",
            "name": {"first": "TestFirstStart", "last": "TestFirstStart"},
            "email": "TestFirstStart@example.com",
            "phone": "9876543210",
            "location": {
                "street": {"number": 1, "name": "TestFirstStart"},
                "city": "TestFirstStart",
                "state": "TestFirstStart",
                "country": "TestFirstStart",
                "postcode": "45454"
            },
            "picture": {"thumbnail": "http://mocked-url.com/thumb.jpg"}
        }
    ]
}


@pytest.mark.django_db
@patch("api.load_users.requests.get")
def test_get_users_from_api_creates_users(mock_get):
    user_count_before = User.objects.count()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = MOCKED_API_RESPONSE

    get_users_from_api(people_count=100, first=False)

    user_count_after = User.objects.count()
    assert user_count_after != user_count_before

    mock_get.assert_called_once()


@pytest.mark.django_db
@patch("api.load_users.requests.get")
def test_get_users_from_api_creates_users_first_start(mock_get):
    User.objects.all().delete()

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = MOCKED_API_RESPONSE

    assert User.objects.count() == 0

    get_users_from_api(people_count=1, first=True)

    assert User.objects.count() == 1