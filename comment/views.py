from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import Article
from .forms import CommentForm

# Create your views here.

@login_required(login_url = '/login/')
def post_comment(request,article_id):
	article = get_object_or_404(Article,id = article_id)
	if request.method == 'POST':
		commtent_form = CommentForm(request.POST)
		if commtent_form.is_valid():
			new_comment = commtent_form.save(commit = False)
			new_comment.article = article
			new_comment.user = request.user
			new_comment.save()
			return redirect(article)
		else:
			return HttpResponse("请重填！")
	else:
		return HttpResponse("错误请求！")
		