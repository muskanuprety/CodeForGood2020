
from django.contrib import admin
from django.urls import path
from website import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.base, name="base"),
    path('admin/', admin.site.urls),
    path('create/', views.create, name="create"),
    path('create2/', views.create2, name="create2"),
    path('register/', views.registerPage, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="website/login.html"), name="register"),



]