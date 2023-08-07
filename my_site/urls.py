"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('about/', views.about_view),
    path('create/', views.create_form_article),

    path('<article>/article/', views.article_detail_view),
    path('<article>/comment/', views.article_comment),
    path('<article>/update/', views.update_article),
    path('<article>/delete/', views.delete_article),

    path('topics/', views.topics_view),
    path('topics/<topic>/subscribe/', views.topic_subscribe),
    path('topics/<topic>/unsubscribe/', views.topic_unsubscribe),

    path('profile/<str:username>/', views.profile_username),
    path('set-password/', views.set_password),
    path('set-userdata/', views.set_userdata),
    path('deactivate/', views.deactivate_profile),
    path('register/', views.register_profile),
    path('login/', views.login_profile),
    path('logout/', views.logout_profile),
    path('articles/', views.get_article_by_preference, name='article-preference'),
    path('article/<int:article_id>/', views.article_detail, name='article-detail'),
]
