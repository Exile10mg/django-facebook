from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signup', views.signup, name='signup'),
  path('upload', views.upload, name='upload'),
  path('follow', views.follow, name='follow'),
  path('search', views.search, name='search'),
  path('profile/<str:pk>', views.profile, name='profile'),
  path('like-post', views.like_post, name='like-post'),
  path('comment_new', views.comment_new, name='comment_new'),
  path('signin', views.signin, name='signin'),
  path('logout', views.logout, name='logout'),
  path('settings', views.settings, name='settings'),
]