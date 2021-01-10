"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from cinema_shop import views

urlpatterns = [
    path('', views.home_view, name="home"),

    path('projections/', views.projection_list_view, name="projections"),
    path('projections/<int:id>/', views.projection_view),
    path('projections/<int:movie_id>/buy-ticket/', views.create_ticket, name="buy-ticket"),
    path('create-projection/', views.projection_create_view),

    path('tickets/', views.card_list_view, name="tickets"),

    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()