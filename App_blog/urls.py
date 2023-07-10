from django.urls import path
from . import views

app_name = 'App_blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>', views.BlogDetails, name='blog_details'),
    path('liked/<pk>/', views.Liked, name='liked'),
    path('unliked/<pk>/', views.UnLiked, name='unliked'),
    path('my-blog/', views.MyBlog.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_bolg'),

]