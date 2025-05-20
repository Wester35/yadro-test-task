from random import randint

from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse, HttpResponse
from api.load_users import get_users_from_api
from api.models import User
from django.views.decorators.csrf import csrf_exempt
from django_tables2 import RequestConfig

from .tables import UserTable
from django.core.paginator import Paginator

def load_users_view(request):
    people_count = int(request.GET.get('limit', 0))
    if people_count > 0:
        get_users_from_api(people_count)
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def index(request):
    if request.method == 'POST':
        count = int(request.POST.get('count'))
        if count > 0:
            get_users_from_api(count, first=False)
        return redirect('/')

    users = User.objects.all().order_by('id')
    table = UserTable(users)
    RequestConfig(request, paginate={"per_page": 20}).configure(table)

    return render(request, 'frontend/index.html', {'table': table})

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
