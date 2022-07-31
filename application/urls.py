from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('add/save/', views.add_save, name='add_save'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/save/<int:id>', views.edit_save, name='edit_save'),
    path('edit/delete/<int:id>', views.edit_delete, name='edit_delete'),
]