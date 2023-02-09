from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('aricle_create/', views.article_create, name='article_create'),
    path('<slug>/', views.article_detail, name='article_detail'),
    path('edit_article/<slug>', views.edit_article, name='edit_article'),
    path('delete_article/<slug>', views.delete_article, name='delete_article'),
    path('<slug>/like', views.like, name='like'),
    path('<slug>/dislike', views.dislike, name='dislike'),
    path('delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('<slug>/comment/<pk>/edit/', views.edit_comment, name='edit_comment'),
]
