"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .views import index, detail, ContentView, ContentListView,ContentDetailView, get_contents_api

app_name = "core"
urlpatterns = [
    path("", ContentView.as_view(), name="index"),
    path("<int:id>", detail, name="detail"),
    path("list", ContentListView.as_view(), name="list"),
    path("list/<int:pk>", ContentDetailView.as_view(), name="detail_page"),
    path("api", get_contents_api, name="api"),
]
