# django imports
from django.views import View
from django.contrib.auth import (
    authenticate ,
    login
)
from django.contrib import messages
from django.shortcuts import redirect

# models import
from django.contrib.auth.models import User

# ============================ Auth Views ===============================
class LoginView(View):
    def post(self , request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        if user:
            login(request, user)
        else:
            messages.warning(request, 'invalid credentials')
        return redirect('/')

class SignUpView(View):
    def post(self , request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User(username=username , password=password)
            user.set_password(password)
            user.save()
            login(request, user)
        except Exception as e:
            print(e)

            messages.warning(request, 'username already exists!')
        return redirect('/')
# ======================================================================================