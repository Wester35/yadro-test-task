import requests
from django.db import IntegrityError
from django.utils.text import slugify
from api.models import User, Location
from django.conf import settings


def get_users_from_api(people_count = 1000, first = True):
    url = f'https://randomuser.me/api/?results={people_count}'
    if User.objects.exists() and first:
        print("Пользователи уже загружены.")
        return

    try:
        response = requests.get(url)
        data = response.json()['results']
    except Exception as e:
        print("Ошибка при загрузке данных из API: ", e)
        return

    for user in data:
        location_data = user['location']
        location, _ = Location.objects.get_or_create(
            street_number=location_data['street']['number'],
            street_name=location_data['street']['name'],
            city=location_data['city'],
            state=location_data['state'],
            country=location_data['country'],
            postcode=location_data['postcode']
        )

        try:
            User.objects.create(
                gender=user['gender'],
                name=user['name']['first'],
                surname=user['name']['last'],
                phone_number=user['phone'],
                email=user['email'],
                location=location,
                picture_thumbnail=user['picture']['thumbnail'],
            )
        except IntegrityError:
            continue