from django.urls import path, include

from post_service.views import post_list, login_validate, login_page

urlpatterns = [
    path('', post_list),
    path(r'login_page/', login_page),
    path(r'login_page/validate/', login_validate),
]
