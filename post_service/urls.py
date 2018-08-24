from django.urls import path

from post_service.views import login, login_validate
from . import views

urlpatterns = [
    path('', views.post_list),
    path('login', login),
    path('login/validate', login_validate)
]