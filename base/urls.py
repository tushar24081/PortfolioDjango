from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.home, name="home"),
	path('posts/', views.posts, name="posts"),
	path('post/<str:slug>', views.post, name="post"),
	path('profile/', views.profile, name="profile"),
	path('create_post/', views.createPost, name="create_post"),
	path('update_post/<str:slug>', views.updatePost, name="update_post"),
	path('delete_post/<str:slug>', views.deletePost, name="delete_post"),
	path('send_email/', views.send_email, name="send_email"),
	path('tag_post/<str:name>', views.tagPosts, name="tag_post")


]