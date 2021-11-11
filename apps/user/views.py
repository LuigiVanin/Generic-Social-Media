from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm, LoginForm

def login_reg(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        
        login_form = LoginForm()
        register_form = RegisterForm()
        ctx = {
            "login": login_form,
            "reg": register_form,
        }
        
        return render(request, 
                    'index.html',
                    context=ctx,
                    status=200)

