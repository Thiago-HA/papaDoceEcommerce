from django.urls import path
from . import views


urlpatterns = [
    path('verifica_pagamento/',  views.verifica_pagamento, name='verifica_pagamento'),

]
 