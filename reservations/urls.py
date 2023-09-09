"""
URL configuration for reservations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from reservationsApp import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.loginView, name="loginView"),
    path("logout/", views.logoutView, name="logoutView"),
    path('add/', views.add, name="add"),
    path('list/', views.list, name="list"),
    path("<int:reservation_id>/delete/", views.delete, name="delete"),
    path("<int:reservation_id>/edit/", views.edit, name="edit"),
    path('users/', views.users, name="users"),
    path('list/b6', views.b6, name="b6"),
    path('list/b7', views.b7, name="b7"),
    path('list/b8', views.b8, name="b8"),
    path('list/b9', views.b9, name="b9"),
    path('list/b10', views.b10, name="b10"),
    path('list/b11', views.b11, name="b11"),
    path('list/b12', views.b12, name="b12"),
    path('list/b13', views.b13, name="b13"),
    path('list/b14', views.b14, name="b14"),
    path('list/b15', views.b15, name="b15"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


