from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import User


class LoginView(View):
    def get(self, request):
        # GET: Zobrazení přihlašovacího formuláře
        return render(request, 'exam_app/login.html')

    def post(self, request):
        # POST: Získání dat z formuláře
        username_val = request.POST.get('username')
        password_val = request.POST.get('password')

        # Ověření uživatele v databázi podle tvého modelu User
        user_exists = User.objects.filter(username=username_val, password=password_val).exists()

        if user_exists:
            # Uživatel existuje -> vytvoření cookies na 24 hodin (86400 sekund)
            response = HttpResponse("Logged in")
            response.set_cookie('logged_in', 'true', max_age=86400)
            return response
        else:
            # Uživatel neexistuje -> smazání cookies
            response = HttpResponse("Login error")
            response.delete_cookie('logged_in')
            return response


from django.shortcuts import render

# Create your views here.
