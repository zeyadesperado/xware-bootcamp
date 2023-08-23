from django.urls import path
from blog import views
urlpatterns = [
    # path('', views.home),
    path('create',views.create_blog, name = 'create_blog'),
    path('home',views.blog_home,name='blog_home'),
    path('myblogs',views.myblogs, name='myblogs'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('' , views.blog_home)
]