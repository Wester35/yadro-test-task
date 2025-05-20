from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('users/', views.users_list_view, name='users_list'),
    path('<int:user_id>/', views.user_detail_view, name='user_detail'),
]