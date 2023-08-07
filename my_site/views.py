from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from first_app.models import Article, Comment, Topic, UserTopicRelationship, UserPreference



def about_view(request):
    return HttpResponse("This is a site where you can find the latest, current world news")

def home_view(request):
    return HttpResponse("Site structure ")

def article_detail_view(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f" Default article - {article}")

def article_comment(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"Comment to article - {article}")

def create_form_article(request):
    return HttpResponse(f"Block_1,Block_2")

def update_article(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"Update to article - {article}")

def delete_article(request: HttpRequest, article: str) -> HttpResponse:
    return HttpResponse(f"Delete to article - {article}")

def topics_view(request):
    return HttpResponse("My topics")

def topic_subscribe(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Subscribe topic - {topic}")

def topic_unsubscribe(request: HttpRequest, topic: str) -> HttpResponse:
    return HttpResponse(f"Unsubscribe topic - {topic}")

def profile_username(request: HttpRequest, username: str) -> HttpResponse:
    return HttpResponse(f"Enter username - {username}")

def set_password(request) :
    return HttpResponse("Enter password")

def set_userdata(request):
    return HttpResponse("Enter userdata")

def deactivate_profile(request):
    return HttpResponse("Deactivate profile")

def register_profile(request):
    return HttpResponse("Profile registration")

def login_profile(request):
    return HttpResponse("Login")

def logout_profile(request):
    return HttpResponse("Logout")

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article)
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


