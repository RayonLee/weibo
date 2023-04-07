from django.db import models
from django.contrib.auth.models import User
from article.models import Article

# Create your models here.

class Favorite(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	article = models.ForeignKey(Article,on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now=True)