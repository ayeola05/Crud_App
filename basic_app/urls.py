from django.urls import path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
   path('', views.Index, name='index'),
   path('list/', views.SchoolView, name='list'),
   path('detail/<int:pk>/', views.SchoolDetail, name='detail'),
   path('create/', views.SchoolCreateView, name='create'),
   path('update/<int:pk>/', views.SchoolUpdateView, name='update'),
   path('delete/<int:pk>/', views.SchoolDeleteView, name='delete'),
   path('register/', views.RegisterView, name='register'),
]
