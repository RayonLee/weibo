from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .forms import UserLoginForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
	if request.method == 'POST':
		user_login_form = UserLoginForm(data = request.POST)
		if user_login_form.is_valid():
			data = user_login_form.cleaned_data
			user = authenticate(username = data['username'],password = data['password'])
			if user:
				login(request,user)
				return redirect("list")
			else:
				return HttpResponse("账号或密码有误，请重新输入！")
		else:
			return HttpResponse("账号或密码输入不合法")
	elif request.method == 'GET':
		if request.user.is_authenticated:
			return render(request, 'users/logined.html')
		else:
			user_login_form = UserLoginForm()
			context = {'form':user_login_form}
			return render(request,'users/login.html',context)
	else:
		return HttpResponse("错误请求！")

def user_logout(request):
	logout(request)
	return redirect("list")

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data = request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit = False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect("list")
        else:
            return HttpResponse("注册输入有误，请重新输入！")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'users/register.html', context)
    else:
        return HttpResponse("错误请求！")

@login_required(login_url = '/login/')
def article_collect(request,id):
	if request.method == 'POST':
		print(id)
		return redirect('detail',id)
	elif request.method == 'GET':
		print(id)
		return redirect('detail',id)
	else:
		return HttpResponse("错误请求！")


@login_required(login_url = '/login/')
def article_collectshow(request):
	print("hello")




def demo(request):
	return render(request,"users/demo.html")


















