from django.shortcuts import redirect, render
from usuarios.models import Usuario


# Create your views here.
def pagina_home(request):
    status = request.GET.get('status')
    return render(request, 'home.html', {'status' : status})

    
