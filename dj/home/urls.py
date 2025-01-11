from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index,name='index'),
    path('create/', views.create,name='create_tweet'),
    path('view/<int:id>/', views.view,name='view'),
    path('edit/<int:id>/', views.edit,name='edit'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('login/', views.User_login,name='login'),
    path('signup/', views.User_signup,name='signup'),
    path('logout/', views.User_logout,name='logout'),
    
    
]
