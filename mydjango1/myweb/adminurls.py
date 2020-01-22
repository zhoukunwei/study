from django.urls import path
from myweb import views

urlpatterns = [
    path('', views.queryUsers),
    path('queryUsers/', views.queryUsers),
    path('openUserAdd/', views.openAdd),
    path('saveUser/', views.saveUser),
    path('openEdit/', views.openEdit),
    path('updateUser/', views.updateUser),
    path('deleteUser/', views.deleteUser),
]
