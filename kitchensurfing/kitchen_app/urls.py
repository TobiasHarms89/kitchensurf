from django.conf.urls import url
from kitchen_app import views

app_name = 'kitchen_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^events/$',views.events,name='events'),
    url(r'^list/$',views.event_list,name='event_list')


]
