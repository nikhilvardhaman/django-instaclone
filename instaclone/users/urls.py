from django.urls import path
from . import views
#localhost:8000/users/index/
urlpatterns = [
    path('index/', views.index, name='users_main_view')
]