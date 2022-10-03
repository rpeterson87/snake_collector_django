from django.contrib import admin
from dj_database_url import path, include

from main_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name="about"),
]
