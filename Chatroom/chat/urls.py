from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.Chat_get),
    url(r'^Send/$',views.Chat_send),
    url(r'^Get_chat/$',views.Chat_get),
    url(r'^make_group/$',views.make_chat_room)
]