from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    # 로그인이 되어있다면,
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form = form.save()
            # 게시글 목록 페이지
            auth_login(request, form)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        # 사용자가 보낸 값 -> form
        form = AuthenticationForm(request, request.POST)
        # 검증
        if form.is_valid():
            # 검증 완료시 로그인!
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    # 조건식으로 직접 작성 해도 된다.
    auth_logout(request)
    return redirect('movies:index')


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    person_color = dict()
    person_color['red'] = person.red
    person_color['grey'] = person.grey
    person_color['yellow'] = person.yellow
    person_color['mint'] = person.mint
    person_color['skyblue'] = person.skyblue
    person_color['dark'] = person.dark
    person_color['white'] = 0
    sum_color = 0
    for value in person_color.values():
        sum_color += value 
    if sum_color:
        for key, value in person_color.items():
            person_color[key] = (value * 100) // sum_color
    else:
        person_color['white'] = 100
    movies = person.like_movies.all()
    context = {
        'person': person,
        'person_color': person_color,
        'movies': movies
    }
    return render(request, 'accounts/profile.html', context)


@permission_required('is_superuser')
def userlist(request):
    users = get_user_model().objects.all()
    context= {
        'users': users,
    }
    return render(request, 'accounts/userlist.html', context)



def management(request, user_name):
    user = get_object_or_404(get_user_model(), username=user_name)
    if user.is_staff:
        user.is_staff = False 
    else:
        user.is_staff = True
    user.save()
    return redirect('accounts:profile', user_name)
