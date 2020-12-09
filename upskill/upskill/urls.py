
from django.contrib import admin
from django.urls import path
from website import views 

urlpatterns = [
	path('', views.base, name="base"),
    path('admin/', admin.site.urls),
    path('create/', views.create, name="create"),
    path('create2/', views.create2, name="create2"),


]