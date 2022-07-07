from django.urls import path

from food import views
from food.views import FoodListView, FoodCreateView, FoodDetailView, FoodUpdateView, FoodDeleteView

app_name = 'food'

urlpatterns = [
    path('list/', views.list_food, name='list'),
    path('add/', views.create_food, name='add'),
    path('detail/<int:pk>/', views.detail_food, name='detail'),
    path('edit/<int:pk>/', views.modify_food, name='edit'),
    path('delete/<int:pk>/', views.delete_food, name='delete'),
]