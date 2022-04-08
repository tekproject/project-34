from django.urls import path
from api import views
from rest_framework.authtoken import views as api_views

urlpatterns = [
    path('', views.home, name='api-home'),

    path('urls', views.urlList, name='URL-all'),
    path('create-url', views.urlCreate, name='URL-all'),

    path('bookmarks', views.myBookMarks, name='bookmark-all'),
    path('create-bookmark', views.bookmarkCreate, name='bookmark-all'),
    
    path('profile', views.profile, name='profile'),

    path('create-user', views.userEntry, name='profile'),
    
    path('update-user', views.userUpdate, name='profile'),
    path('user-update-password', views.passwordUpdate, name='User-Update-password'),

    # path('users', views.user.userList, name='User-all'),
    # path('user/<str:pk>', views.user.userDetail, name='User-Detail'),
    # path('user-profile', views.user.loggedUser, name='User-logged'),
    # path('user-create', views.user.userEntry, name='User-Create'),
    # path('user-update/<str:pk>', views.user.userUpdate, name='User-Update'),
    # path('user-update-password/<str:pk>', views.user.passwordUpdate, name='User-Update-password'),
    # path('user-reset-password/<str:pk>', views.user.resetPassword, name='User-Reset-password'),
    # path('admin-user-update/<str:pk>', views.user.adminUserUpdate, name='Admin-User-Update'),
    # path('user-delete/<str:pk>', views.user.userDelete, name='User-Delete'),

    path('api-login', api_views.obtain_auth_token)
]