from django.shortcuts import get_object_or_404,render,redirect
from .models import Favorite
from article.models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_favorite(request,article_id):
	article = get_object_or_404(Article, id = article_id)
	favorite = Favorite(user = request.user,article = article)
	favorite.save()
	return redirect('detail',id=article.id)

def remove_favorite(request,article_id):
	print("hello")
	article = get_object_or_404(Article,id = article_id)
	favorite = Favorite.objects.filter(user = request.user,article = article)
	favorite.delete()
	return redirect('detail',id=article.id)

@login_required
def favorite_list(request):
	favorites = Favorite.objects.filter(user = request.user)
	return render(request,'article/favorite_list.html',{'favorites':favorites})