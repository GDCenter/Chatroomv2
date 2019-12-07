from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Chat,Group_chat
from django.db.models import Q
from user.models import UserProfile
# Create your views here.

"""
返回与自己有关的聊天列表，找到对方id，并将对方的数据获取到
数据有：
    名字，头像

"""
def Chat_list(request):
    if request.method == 'GET':
        #返回get页面
        return render(request,'chat.html')
    if request.method == 'POST':
        #ajax获取数据
        #检测session中的用户数据是否与ajax的数据是否一致
        json_str = request.body
        if not json_str:
            #前段传的数据有误
            result = {'code':201,'error':'Please POST data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        #获取当前用户的id
        user_id = json_obj.get('user_id')
        # 去聊天数据中匹配
        #找到是自己发出的并不是公共聊天室的
        try:
            list_chat= Chat.objects.filter(Q(user_self_id=user_id) & Q(target_Pubroom=None))
        except Exception as e:
            print(e)
            result = {'code':202,'error':'sql data error'}
            return JsonResponse(result)
        if list_chat == None:
            result = {'code':203,'error':'None'}
            return JsonResponse(result)


        list_id = [list.target_user for list in list_chat]

        #list_id 要去重
        list_id=set(list_id)
        # 返回给前段头像，头像，id,名字
        list_user = []
        for user_id in list_id:
            user = UserProfile.objects.get(id=user_id)
            user_info ={}
            user_info['id'] =user.id
            user_info['username'] =user.username
            user_info['img']=user. avatar
            list_user.append(user_info)
        result = {'code':200,'data':list_user}
        return JsonResponse(result)

def Pub_list(request):
    if not request.method == 'POST':
        result = {'code':204,'error':'Go out and turn left'}
        return JsonResponse(result)
    else:
        #从前段数据中找出用户信息
        #根据用户信息找到与改用户所有相关的帖子
        # 将所有与该用户相关的帖子发送给前段
        json_str = request.body
        if not json_str: #前段传递数据有误
            result = {'code':201,'error':'Please POST data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        user_id = json_obj.get('user_id')
        #获得user_id后去查数据库，找与之匹配的数据
        try:
            chat_pub = Chat.objects.filter(Q(user_self_id=user_id) & Q(target_user=None))
        except Exception as e:
            print(e)
            result = {'code':202,'error':'sql data error'}
            return JsonResponse(result)
        pub_id_list=[pubid.target_Pubroom for pubid in chat_pub]
        pub_id_list = set(pub_id_list)
        #返回前段公共聊天室数据有一下：
        # 聊天室名字 roomname，id
        pub_list = []
        for pub_id in pub_id_list:
            pub = Group_chat.objects.get(id=pub_id)
            pub_info={}
            pub_info['name'] = pub.roomname
            pub_info['id'] = pub.id

            pub_list.append(pub_info)
        result = {'code':200,'data':pub_list}
        return JsonResponse(result)

