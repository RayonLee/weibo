from django import forms
from .models import Article

#继承modelform类和定义模型属性与模型关联起来
class ArticleForm(forms.ModelForm):
	#内部类，指明数据来源和表单中的数据模型字段
	class Meta:
		model = Article
		fields = ('title','body')
