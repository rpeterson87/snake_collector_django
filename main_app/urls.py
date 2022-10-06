from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('snakes/', views.SnakeList.as_view(), name="snake_list"),
    path('snakes/new/', views.SnakeCreate.as_view(), name="snakes_create"),
    path('snakes/<int:pk>/', views.SnakesDetail.as_view(), name="snakes_detail"),
    path('snakes/<int:pk>/update', views.SnakeUpdate.as_view(), name="snakes_update"),
    path('snakes/<int:pk>/delete', views.SnakeDelete.as_view(), name="snakes_delete"),
    path('snakes/<int:pk>/data/new/', views.SnakesCreate.as_view(), name="snake_create"),
    path('snakes/<int:pk>/data/<int:snake_pk>/', views.SnakelistDataAssoc.as_view(), name="snakelist_snake_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
