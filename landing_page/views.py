from django.shortcuts import render

# Create your views here.
def home(request):
<<<<<<< HEAD:landing_page/views.py
    return render(request, 'landing/landing.html')
=======
    return render(request, 'landing/index.html')

def login_view(request):
    return render(request, 'landing/login.html')
>>>>>>> 355b8a5 (Landing Page updates):Online_Store/landing_page/views.py
