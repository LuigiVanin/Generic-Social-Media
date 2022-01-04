from functools import reduce
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib import auth
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import User

def login_reg(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profile', acc=request.user.username)
        
        login_form = LoginForm()
        register_form = RegisterForm()
        ctx = {
            "login": login_form,
            "reg": register_form,
        }
        return render(
            request,
            'index.html',
            context=ctx,
            status=200
        )

    if request.method == "POST":
        data = request.POST
        user = auth.authenticate(
            request,
            username=data["username"],
            password=data["password"]
        )
        
        if user is not None:
            auth.login(request, user)
            return redirect('profile', acc=request.user.username)
        else:
            return redirect('login')
    
        
def registration(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        data = request.POST
        if data["password"] == data["password2"]:
            user: User = User.objects.create_user(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
                bio=data["bio"],
                gender=data["gender"]
            )
            user.save()
            return redirect('login')


@login_required(login_url='login')
def profile(request: HttpRequest, acc: str) -> HttpResponse:
    if request.method == "GET":
        my_acc: bool = False
        user: User = User.objects.filter(username=acc).first()
        if acc == request.user.username:
            my_acc = True
        ctx = {
            "data": user,
            "me": my_acc,
        }
        return render(
            request,
            "profile.html",
            context=ctx,
            status=200
        )
      
        
@login_required(login_url='login')
def search_result(request: HttpRequest) -> HttpResponse:
    
    if request.method == "GET":
        search_param = request.GET["search"]
        users: User = None
        if search_param.strip() != "":
            if search_param.strip() == "/all":
                search_param=""
            query = (
                Q(first_name__icontains=search_param) |
                Q(last_name__icontains=search_param) |
                Q(username__icontains=search_param)
            )
            users: User.objects = User.objects.filter(query)
            if users.exists():
                users = users.all()
            else:
                users = None
        else:
            return redirect('profile', acc=request.user.username)
        ctx = {
            "data": users
        }
        print(users)
        return render(
            request,
            "search_result.html",
            context=ctx
        )


@login_required(login_url='login')
def new_img(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        to_updt = request.FILES["new_img"]
        user: User = User.objects.filter(username=request.user.username).first()
        if to_updt is not None:
            user.profile_pic = to_updt
        user.save()
        return redirect('profile', acc=request.user.username)

def logout(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')