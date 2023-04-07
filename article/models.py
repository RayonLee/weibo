from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Article(models.Model):
	# 文章id作主键
	id = models.AutoField(primary_key = True)
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)


	# 正文
	body = models.TextField()

	created = models.DateTimeField(default = timezone.now)
	updated = models.DateTimeField(auto_now = True)

	total_views = models.PositiveIntegerField(default = 0)

	if_collect_flag = models.BooleanField(default = False)

	def get_absolute_url(self):
		return reverse('detail',args=[self.id])