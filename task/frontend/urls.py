from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.user_detail_view, name='user_detail'),
    path('random/', views.random_user_view, name='random_user'),

]