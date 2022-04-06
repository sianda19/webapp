from . import views
from django.urls import path

urlpatterns = [path('',views.home,name='home'),
path('sign',views.Sign,name='sign'),
path('submit',views.submit,name='submit'),
path('write',views.write,name='write'),
path('article',views.article,name='article'),
path('log',views.log,name='log'),
path('logpage',views.logpage,name='logpage'),
path('home',views.homes,name='home'),
path('logout',views.logout,name='logout'),
path('mypost',views.my_post,name='mypost'),
path('add/<int:article>', views.comments, name='comments'),
path('add/comment',views.post_comment,name='comment'),

path('add/home',views.prevent_home_error,name='home'),
path('add/mypost',views.prevent_mypost_error,name='mypost'),
path('add/write',views.prevent_write_error,name='write'),
path('add/logpage',views.prevent_logpage_error,name='logpage'),
path('add/sign',views.prevent_sign_error,name='sign'),
path('add/logout',views.prevent_logout_error,name='logout'),
path('add/article',views.prevent_article_error,name='article'),
path('add/submit',views.prevent_save_error,name='submit'),
path('add/log',views.prevent_log_error,name='log'),
path('search',views.search,name='search')

]




