"""weibo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#app view
import article.views
import users.views
import comment.views
import favorites.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',article.views.article_list,name = 'list'),
    #尖括号定义需要传递的参数<>
    path('detail/<int:id>',article.views.article_detail,name = 'detail'),
    path('create/',article.views.article_create,name = 'create'),
    path('delete/<int:id>',article.views.article_delete,name= 'delete'),
    path('update/<int:id>',article.views.article_update,name = 'update'),
    path('collect/<int:id>',users.views.article_collect,name = 'collect'),
    path('mycollect',users.views.article_collectshow,name = 'collect_show'),
    path('login/',users.views.user_login,name = 'login'),
    path('logout/',users.views.user_logout,name = 'logout'),
    path('register/',users.views.user_register,name = 'register'),
    path('post-comment/<int:article_id>/', comment.views.post_comment, name='post_comment' ),
    path('favorite_list/',favorites.views.favorite_list,name = 'favorite_list'),
    path('favorite/<int:article_id>',favorites.views.add_favorite,name = 'add_favorite'),    
    path('favorite/remove/<int:article_id>',favorites.views.remove_favorite,name = 'remove_favorite'),      
    ]









































