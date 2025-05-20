from django.shortcuts import render
from django.http import JsonResponse
from .load_users import get_users_from_api
from .models import User
from django.core.paginator import Paginator

def load_users_view(request):
    people_count = int(request.GET.get('limit', 0))
    if people_count > 0:
        get_users_from_api(people_count)
    return JsonResponse({'status': 'ok'})

def users_list_view(request):
    page = int(request.GET.get('page', 1))
    page_size = 50
    users = User.objects.all().order_by('id')
    paginator = Paginator(users, page_size)
    page_obj = paginator.get_page(page)
    users_data = [{
        'id': user.id,
        'gender': user.gender,
        'name': user.name,
        'surname': user.surname,
        'phone': user.phone_number,
        'email': user.email,
        'address': (f"{user.location.postcode}, {user.location.country}, "
                    f"{user.location.state}, {user.location.city}, "
                    f"{user.location.street_number}, {user.location.street_name}"
                    if user.location else "Адрес не указан")

    } for user in page_obj.object_list]

    return JsonResponse({
        'users': users_data,
        'page': page,
        'num_pages': paginator.num_pages,
        'total': paginator.count,
    })
