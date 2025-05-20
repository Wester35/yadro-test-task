from random import randint

from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from api.load_users import get_users_from_api
from api.models import User
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

def index(request):
    return render(request, 'frontend/index.html')

def user_detail_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'frontend/user_detail.html', {'user': user})

def random_user_view(request):
    count = User.objects.count()
    if count == 0:
        return render(request, 'no_users.html')
    random_index = randint(1, count)
    random_user = User.objects.all()[random_index]
    return render(request, 'frontend/user_detail.html', {'user': random_user})