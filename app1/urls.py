from django.urls import path
from . import views
urlpatterns = [
    path('', views.todoList ,name='list'),
    path('details/<int:myid>', views.todoDetails,name='details'),
    path('add/', views.todoCreate,name='add'),
    path('deleted/<int:id>', views.todoDelete,name='deleted'),
    path('edit/<int:id>', views.todoEdit,name='edit'),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]