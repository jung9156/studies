from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

bootstrap_color = {
        'red': 'danger',
        'grey': 'secondary',
        'yellow': 'warning',
        'mint': 'success',
        'skyblue': 'primary',
        'dark': 'dark'
    }
# Create your views here.
def index(request):
    colors = ['red', 'grey', 'yellow', 'mint', 'skyblue', 'dark']
    if request.user.is_authenticated:
        u_c = request.user.color
        articles = Article.objects.order_by('-pk').filter(color = u_c)
    else:
        articles = Article.objects.order_by('-pk')
        u_c = 'white'
    article_number_dict = {}
    for color in colors:
        article_number = get_user_model().objects.filter(color=color).count()
        article_number_dict[color] = article_number
    article_number_dict['best'] = sorted(article_number_dict.items(), key = (lambda x: x[1]), reverse=True)[0][0]
    article_number_dict['best_bootstrap'] = bootstrap_color[article_number_dict['best']]
    context = {
        'articles': articles,
        'article_color': u_c,
        'article_number_dict': article_number_dict,
    }
    return render(request, 'communities/index.html', context)


def article_color(request, article_color):
    colors = ['red', 'grey', 'yellow', 'mint', 'skyblue', 'dark']
    articles = Article.objects.order_by('-pk').filter(color = article_color)
    article_number_dict = {}
    for color in colors:
        article_number = get_user_model().objects.filter(color=color).count()
        article_number_dict[color] = article_number
    article_number_dict['best'] = sorted(article_number_dict.items(), key = (lambda x: x[1]), reverse=True)[0][0]
    article_number_dict['best_bootstrap'] = bootstrap_color[article_number_dict['best']]
    context = {
        'articles': articles,
        'article_color': article_color,
        'article_number_dict': article_number_dict,
    }
    return render(request, 'communities/index.html', context)


@login_required
def create(request, article_color):
    msg = False
    user = request.user
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if user.is_staff or request.user.color == article_color or article_color == 'white':
            if form.is_valid():
                article = form.save(commit=False)
                article.color = article_color
                article.user = request.user 
                article.save()
                return redirect('communities:color', article_color)
        else:
            msg = '게시판 확인을 해주세요. 권한이 부족합니다.'
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'article_color': article_color,
        'msg': msg,
    }

    return render(request, 'communities/form.html', context)
        
@login_required
def detail(request, article_color, article_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = get_object_or_404(Article, pk=article_pk)
            comment.user = request.user
            comment.save()
        return redirect('communities:detail', article_color, article_pk)

    else:
        article = get_object_or_404(Article, pk = article_pk)
        form = CommentForm()
        comments = Comment.objects.order_by('-pk').filter(article = article)
        context = {
            'article': article,
            'form': form,
            'comments': comments
        }
        return render(request, 'communities/detail.html', context)


@login_required
def delete(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if article.user == request.user:
        article.delete()
    return redirect('communities:index')

@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('communities:detail', article_color, article_pk)

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article_u = form.save(commit = False)
                article_u.color = article.color
                article_u.user = request.user 
                article_u.save()
                return redirect('communities:detail', article.color, article_u.pk)
        else:
            form = ArticleForm(instance = article)
        context = {
            'form': form,
        }
        return render(request, 'communities/form.html', context)
    return redirect('communities:index')