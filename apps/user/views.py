from pydoc import doc
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib import auth
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Friends, User

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
        friends: Friends = Friends.objects.filter(owner=request.user.id)
        friends = [i.friend for i in friends]
        if acc == request.user.username:
            my_acc = True
        ctx = {
            "data": user,
            "me": my_acc,
            "friends": friends,
        }
        print(user in friends)
        return render(
            request,
            "profile.html",
            context=ctx,
            status=200
        )
      
   
@login_required(login_url='login')    
def make_friend(request: HttpRequest, friend):
    if request.method == "GET":
        friend = User.objects.filter(username=friend).first()
        if friend is None:
            return redirect('profile', acc=request.user.username)
        
        user = User.objects.filter(username=request.user.username).first()
        friendship = Friends.objects.create(owner=user,
                                            friend=friend)
        friendship.save()
        return redirect('profile', acc=friend.username)       
 
 
@login_required(login_url='login')
def remove_friend(request: HttpRequest, friend):
    if request.method == "GET":
        query = (Q(owner=request.user.id) & 
                 Q(friend=User.objects.filter(username=friend).first().id))
        friend=Friends.objects.filter(query).first()
        friend.delete()
        return redirect('profile', acc=friend.friend.username) 
    
    
def show_all_friends(request: HttpRequest):
    if request.method == "GET":
        friends = Friends.objects.filter(owner=request.user.id).all()
        friends = [i.friend for i in friends]
        ctx = {
            "data":friends,
            "friends": friends,
        }
        return render(request,
            "search_result.html",
            context=ctx
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
        user_owner = Friends.objects.filter(owner=request.user.id).all()
        friends = [i.friend for i in user_owner]
        print(friends)
        ctx = {
            "data": users,
            "friends": friends
        }
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