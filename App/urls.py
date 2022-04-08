from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from App.views import Signup,Search_users
urlpatterns=[
    path('',views.index,name = 'index'),
    path('signup/', Signup, name='signup'),
    path('newpost/', views.NewPost, name='newpost'),
    path('search_users/',Search_users, name='search_users'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
]