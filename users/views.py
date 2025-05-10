from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.admin.views.decorators import staff_member_required
from app.forms import *
from cart.cart import Cart

# Create your views here.
# Личный кабинет
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

def logout_view(request):
    logout(request)
    return redirect('login')

# Личный кабинет
@login_required
def account_view(request):
    return render(request, 'users/account.html')


