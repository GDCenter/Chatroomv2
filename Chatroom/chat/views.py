from django.shortcuts import render
from django.http import JsonResponse
from group_chat.models import Chat,Group_chat
import json
from django.db.models import Q
from user.models import UserProfile
# Create your views here.

#实现客户端建立聊天

#用户建立群聊，
def chat(request):
    if request.method == 'GET':
        render(request,'chat.html')
def make_chat_room(request):
    if not request.method == 'POST':
        result = {'code':301,'error':'Go out and turn left'}
        return JsonResponse(result)
    else:
        json_str = request.body
        json_obj = json.loads(json_str)
        #前端传递来的是，要建立的群聊名称
        roomname = json_obj['roomname']
        try:
            room = Group_chat.objects.create()
            room.roomname = roomname
        except Exception as e:
            print(e)
            #聊天室创建失败后返回的状态码
            result = {'code':302,'error':'SQL error'}
            return JsonResponse(result)

        result = {'code':200,'data':'OK'}
        #创建成功后返回一个状态码
        return JsonResponse(result)

def Chat_send(request):
    #前端发送消息到服务器
    #第一步，判断request类型
    if not request.method == 'POST':
        result = {'code': 301, 'error': 'Go out and turn left'}
        return JsonResponse(result)
    else:
        #规定前端发送的数据，如果是往公共聊天室发送，则将target_Pubroom的id传递过来
        json_str = request.body
        json_obj = json.loads(json_str)
        target_Pubroom = json_obj.get('target_Pubroom',None)
        target_user = json_obj.get('target_user',None)
        user_id = request.session['userinfo']['id']
        content = json_obj.get('content')
        try:
            chat= Chat.objects.create()
            chat.target_Pubroom=target_Pubroom
            chat.target_user=target_user
            chat.user_self_id=user_id
            chat.content=content
            chat.save()
        except Exception as e:
            print(e)
            result = {'code':302,'error':'发送失败'}
            return JsonResponse(result)
        result = {'code':200,'data':'OK'}
        return JsonResponse(result)

def Chat_get(request,time=None):
    """

    :param request:
    :param time: 将最后一条消息的创建时期带过来，将数据库中的记录时间对比，晚点就发出去
    :return:
    """
    # 前端获取消息更新
    if  request.method != "POST":

        return render(request,'index.html')
    id = request.session['userinfo']['id']
    try:
        message =  Chat.objects.filter(Q(target_user=id) & Q(created_time__gt =time))
        if len(message)<=0:#没消息
            result = {'code':205,'error':'no message'}
            return JsonResponse(result)
        else:
            data_list = []
            for info  in message:
                data ={}
                data['content'] = info.content
                data['time'] = info.created_time
                user_info = UserProfile.objects.get(id=info.user_self_id)
                data['id'] = user_info.id
                data['username'] = user_info.username
                data['avatar'] = user_info.avatar
                data_list.append(data)
            result = {'code':200,'data':data_list}
            return JsonResponse(result)


    except Exception as e:
        print(e)




