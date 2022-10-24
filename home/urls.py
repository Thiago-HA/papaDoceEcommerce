

from django.urls import path
from . import views


urlpatterns = [
    path('valida_user_home/',  views.valida_user_home, name='valida_user_home'),
]


