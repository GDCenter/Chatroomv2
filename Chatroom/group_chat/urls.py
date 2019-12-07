from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^Getchat/$',views.Chat_list),
    url(r'^GetPubChat$',views.Group_chat)

]