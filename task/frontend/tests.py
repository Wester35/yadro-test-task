import pytest
from django.urls import reverse
from unittest.mock import patch
from api.models import User, Location


@pytest.mark.django_db
@patch("frontend.views.RequestConfig.configure")
def test_index_get(mock_configure, client):
    mock_configure.side_effect = lambda table: None

    location = Location.objects.create(
        street_number=778,
        street_name='streetT',
        city='TestCity',
        state='TestState',
        country='TestCountry',
        postcode='56565'
    )
    user = User.objects.create(
        name='Mercedes',
        surname='Benz',
        gender='female',
        phone_number='123',
        email='mercedes@example.com',
        location=location
    )

    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert "Mercedes" in response.content.decode()


@pytest.mark.django_db
@patch('frontend.views.get_users_from_api')
def test_index_post(mock_get_users, client):
    response = client.post(reverse('index'), data={'count': '5'})
    mock_get_users.assert_called_once_with(5, first=False)
    assert response.status_code == 302
    assert response.url == '/'

@pytest.mark.django_db
def test_user_detail_view(client):
    location = Location.objects.create(
            street_number=77,
            street_name='streetT',
            city='TestCity',
            state='TestState',
            country='TestCountry',
            postcode='56565'
    )
    user = User.objects.create(name='Gleb', surname='Whatt', gender='male',
                               phone_number='777', email='gleb@example.com',
                               location=location)
    response = client.get(reverse('user_detail', args=[user.id]))
    assert response.status_code == 200
    assert b'Gleb' in response.content

@pytest.mark.django_db
def test_random_user_view_no_users(client):
    response = client.get(reverse('random_user'))
    assert response.status_code == 200
