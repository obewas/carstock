from . import views
from django.urls import path

urlpatterns = [
    path('', views.CarListView.as_view()),
    path('create/', views.CarCreateView.as_view(), name='create'),
    path('<pk>/update', views.CarUpdateView.as_view(), name='update'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('delete/<pk>/', views.DeleteView.as_view(), name='delete'),
    path('total/' , views.total_cost, name='total'),
]