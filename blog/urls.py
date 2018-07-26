from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('categories/<category_slug>', views.category, name='category'),
    path('blog/<int:blog_id>',views.blog,name='blog')
]
