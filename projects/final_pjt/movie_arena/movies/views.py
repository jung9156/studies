from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
import requests
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Movie, Rate
from django.http import JsonResponse
from .forms import MovieForm, GenreForm
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    user = request.user
    # if user.is_authenticated:
    #     user_genre = int(user.genre)
    # else:
    #     user_genre = 0
    context ={
        'movies' : movies,
        'page_obj': page_obj,
        # 'user_genre': user_genre,
    }
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    params = {'key': 'AIzaSyBUD7jlGdoFmGdAmcdVca5xBKBfQmsA2R0', 'part': 'snippet', 'type': 'video', 'q': f'{movie.title}+trailer'}
    res = requests.get('https://www.googleapis.com/youtube/v3/search', params=params).json()
    user = request.user
    if user.is_authenticated:
        if movie.like_users.filter(pk=user.pk).exists():
            rate = user.rate_set.filter(movie=movie)[0].rate
        else:
            rate = 0
    else:
        rate = 0
    context = {
        'movie': movie,
        'rate': rate,
        'res': res,
    }
    return render(request, 'movies/movie_detail.html', context)

def like(request, movie_pk, star_rate):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    star_value = star_rate - 5
    if movie.like_users.filter(pk=user.pk).exists():
        s_rate = user.rate_set.filter(movie=movie)
        value = s_rate[0].rate - 5
        s_rate.delete()
        liked = False
        user.red -= movie.red * value
        user.grey -= movie.grey * value 
        user.yellow -= movie.yellow * value
        user.mint -= movie.mint * value
        user.skyblue -= movie.skyblue * value
        user.dark -= movie.dark * value
    else:
        movie.like_users.add(user)
    liked = True
    user_color = dict()
    user.red += movie.red * star_value
    user.grey += movie.grey * star_value
    user.yellow += movie.yellow * star_value
    user.mint += movie.mint * star_value
    user.skyblue += movie.skyblue * star_value
    user.dark += movie.dark * star_value
    user_color['red'] = user.red
    user_color['grey'] = user.grey
    user_color['yellow'] = user.yellow
    user_color['mint'] = user.mint
    user_color['skyblue'] = user.skyblue
    user_color['dark'] = user.dark
    user.color = max(user_color.keys(), key = (lambda x: user_color[x]))
    user.save()
    rate = Rate(user=user, rate=star_rate, movie=movie)
    rate.save()
    context = {
        'rate': star_rate,
        'liked': liked,
    }
    return JsonResponse(context)

def recommend(request, username):
    bootstrap_color = {
        'red': 'danger',
        'grey': 'secondary',
        'yellow': 'warning',
        'mint': 'success',
        'skyblue': 'primary',
        'dark': 'dark'
    }
    user = get_object_or_404(get_user_model(), username=username)
    movies = Movie.objects.filter(~Q(like_users=user))
    user_color = dict()
    user_color['red'] = user.red
    user_color['grey'] = user.grey
    user_color['yellow'] = user.yellow
    user_color['mint'] = user.mint
    user_color['skyblue'] = user.skyblue
    user_color['dark'] = user.dark
    sorted_user = sorted(user_color.items(), key = (lambda x: x[1]), reverse=True)
    recommend_list = []
    for i in range(3):
        recommend = dict()
        if sorted_user[i][0] == 'mint':
            first_movies = movies.filter(mint=1)[:6]
            second_movies = movies.filter(mint=1)[6:12]
            recommend['ment'] = '두근두근 콩닥콩닥 당신의 연애세포를 깨울 영화!'
        elif sorted_user[i][0] == 'red':
            first_movies = movies.filter(red=1)[:6]
            second_movies = movies.filter(red=1)[6:12]
            recommend['ment'] = '화끈한 액션! 짜릿한 모험! 스트레스 타파!!'
        elif sorted_user[i][0] == 'grey':
            first_movies = movies.filter(grey=1)[:6]
            second_movies = movies.filter(grey=1)[6:12]
            recommend['ment'] = '영화로 배우는 역사! 그때 그 시절 속으로~'
        elif sorted_user[i][0] == 'yellow':
            first_movies = movies.filter(yellow=1)[:6]
            second_movies = movies.filter(yellow=1)[6:12]
            recommend['ment'] = '감성적인 그대에게 띄우는 영화'
        elif sorted_user[i][0] == 'skyblue':
            first_movies = movies.filter(skyblue=1)[:6]
            second_movies = movies.filter(skyblue=1)[6:12]
            recommend['ment'] = '당신의 상상력을 만족시킬 영화!'
        elif sorted_user[i][0] == 'dark':
            first_movies = movies.filter(dark=1)[:6]
            second_movies = movies.filter(dark=1)[6:12]
            recommend['ment'] = '팬티는 챙기셨죠? 당신의 이불을 적실 영화!'
        recommend['first_movies'] = first_movies
        recommend['second_movies'] = second_movies
        recommend['bg'] = bootstrap_color[sorted_user[i][0]]
        
        
        recommend_list.append(recommend)
    

    context = {
        'recommend_list': recommend_list
    }
    return render(request, 'movies/recommend.html', context)

def moviecreate(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                form = form.save()
                return redirect('movies:index')
            else:
                return redirect('movies:index')
        else :
            form = MovieForm()
        context = {
            'form': form,

        }
        return render(request,'movies/form.html',context)
    else:
        return redirect('accounts:login') 