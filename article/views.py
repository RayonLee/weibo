from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#导入数据模型Article
from .models import Article
from .forms import ArticleForm
from comment.models import Comment
from favorites.models import Favorite

# Create your views here.

def article_list(request):
	if request.GET.get('order') == 'total_views':
		article_list = Article.objects.all().order_by('-total_views')
		order = 'total_views'
	else:
		article_list = Article.objects.all().order_by('-created')
		order = 'created'
	context = {'articles':article_list,'order':order}
	return render(request,'article/list.html',context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    article.total_views += 1
    article.save(update_fields=['total_views'])
    comments = Comment.objects.filter(article=id)
    favorites = None
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user, article=article)
        for favorite in favorites:
            print(favorite.user,favorite.article)
    context = {'article': article, 'comments': comments, 'favorites': favorites}
    return render(request, 'article/detail.html', context)


@login_required(login_url = '/login/')
def article_create(request):
	if request.method == 'POST':
		article_post_form = ArticleForm(data = request.POST)
		if article_post_form.is_valid():
			new_article = article_post_form.save(commit = False)
			new_article.author = request.user
			new_article.save()
			return redirect("list")
		else:
			return HttpResponse("请重新填写！")

	else:
		article_post_form = ArticleForm()
		context = {'article_post_form':article_post_form}
		return render(request,'article/create.html',context)


def article_delete(request,id):
	if request.method == 'POST':	
		article = Article.objects.get(id = id)
		article.delete()
		return redirect("list")
	else:
		return HttpResponse("错误请求！")


def article_update(request,id):
	article = Article.objects.get(id = id)
	article_post_form = ArticleForm()
	context = {'article':article,'article_post_form':article_post_form}
	if request.method == 'POST':
		article_post_form = ArticleForm(data = request.POST)
		if article_post_form.is_valid():
			article.title = request.POST['title']
			article.body = request.POST['body']
			article.save()
			# 返回视图article_detail
			return redirect('detail',id = id)
		else:
			return HttpResponse("请重填！")
	else:
		return render(request,'article/update.html',context)




























