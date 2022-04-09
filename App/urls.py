from django.urls import path,include
from . import views
from django.contrib.auth import views as authViews
from App.views import Signup,Search_users,NewPost,rate
urlpatterns=[
    path('',views.index,name = 'index'),
    path('signup/', Signup, name='signup'),
    path('newpost/', views.NewPost, name='newpost'),
    path('search_users/',Search_users, name='search_users'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('posts/<id>/',views.posts,name = 'posts'),
    # path('rate/', rate, name='rate'),
    path('rate/<id>/',views.rate,name = 'rate'),
    path('api/profile',views.ProfileList.as_view()),
    path('api/posts',views.PostList.as_view()),
    path('profile/<id>/',views.profile,name = 'profile')
]