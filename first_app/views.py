from django.shortcuts import render, get_object_or_404
from .models import Article, Comment, UserPreference
from django.contrib.auth.models import User

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = comments = article.comments.all()
    return render(request, 'article_detail.hhtml', {'article': article, 'comments': comments})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(author=user)
    return render(request, 'user_profile.html', {'user': user, 'articles': articles})

def get_article_by_preference(request):
    user = request.user
    if not user.is_authenticated:
        articles = []
    else:
        user_preference, created = UserPreference.objects.get_or_create(user=user)
        liked_tags = user_preference.liked_tags.all()
        articles = Article.objects.filter(tags__in=liked_tags).distinct().order_by('-popularity')
        return render(request, 'article_list.html', {'articles': articles})



