from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('project_details/<int:project_id>/', views.project_details, name='project_details'),
]
