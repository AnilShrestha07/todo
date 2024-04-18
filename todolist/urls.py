from django.urls import path

from . import views


urlpatterns = [
    path('todolist', views.handle_todolist, name='todolist'),
    path('update/<int:pk>/update', views.update, name='update'),
    path('delete/<int:pk>/delete', views.delete, name='delete')
    
    
]
