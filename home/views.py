from django.shortcuts import render

# Create your views here.
def pagina_home(request):
    return render(request, 'home.html')