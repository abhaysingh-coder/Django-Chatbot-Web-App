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
    path('logout/', views.logout_view, name='logout'),
]