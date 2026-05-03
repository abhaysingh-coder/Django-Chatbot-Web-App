from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('reset/', views.reset_session, name="reset_session"),
    path('signup/', views.signup, name='signup'),
    path('forget/', views.forget, name='forget'),
    path('user/', views.user_page, name='user_page'),
    path('user-admin/', views.user_admin_panel, name='user_admin_panel'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('update-user/<int:id>/', views.update_user, name='update_user'),
]