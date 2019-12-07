from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.http import JsonResponse
import json
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == 'POST':
        # id = models.IntegerField(primary_key=True)
        # username = models.CharField('用户名', max_length=11, )
        # nickname = models.CharField('昵称', max_length=30)
        # password = models.CharField('密码', max_length=40)
        # avatar = models.ImageField('头像', max_length=100)

        username = request.POST.get('username')
        password = request.POST.get('password')
        password2= request.POST.get('password2')
        nickname = request.POST.get('nickname')

        if password !=password2:
            return HttpResponse('你输入的密码不一致')
        try:
            user = UserProfile.objects.get(username=username)
            if user:
                return HttpResponse('该用户已存在')
        except Exception as e:
            print(e)

        user = UserProfile.objects.create()
        user.username = username
        user.password = password
        user.nickname = nickname
        user.save()

        return HttpResponseRedirect('/user/login')




def login(request):
    #post方式登录
    if request.method == 'GET':
        username = request.COOKIES.get('username','')
        return render(request,'login.html')

    elif request.method == 'POST':
        remember = request.POST.get('remeber','')
        username = request.POST.get('username','')
        password= request.POST.get('password','')

        #验证用户名，密码是否正确
        try:
            user = UserProfile.objects.get(name = username,password=password)

            #在当前连接的session中记录当前用户的信息
            request.session['userinfo'] ={
                'username':user.username,
                'id':user.id
            }
        except  Exception as e :
            print(e)


        #处理cookies
        response = HttpResponseRedirect('/chat')
        if remember:
            response.set_cookie('username',username,7*23*60*60)
        else:
            response.delete_cookie('username')
        return response

def logout(request):
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/login')

def user_avatar(request,username):
    #上传图片思路
    #1.前端-> form提交,并且content-type 要改成multipart/form-data
    #2.后端只要拿到post提交,request.FILES['avatar']
    #    注意:由于目前django获取put请求的multipart数据较为复杂,故改为post获取multipart

    if not request.method == 'POST':
        print(request.method)
        result = {'code':210,'error':'Please use POST'}
        return JsonResponse(result)
    users = UserProfile.objects.filter(username=username)
    if not users :
        result={'code':208,'error':"The user is not existed"}
        return JsonResponse(result)
    if request.FILES.get('avatar'):
        #
        users[0].avatar = request.FILES['avatar']
        users[0].save()
        result={'code':200,'username':username}
        return JsonResponse(result)
    else:
        result = {'code':211,'error':'Plaeas give me avatar'}
        return JsonResponse(result)
