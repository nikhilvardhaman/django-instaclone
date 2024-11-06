from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

#localhost:8000/users/index/
urlpatterns = [
    path('index/', views.index, name='users_main_view'),

    path('add/', views.create_user, name='create_user_api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_api'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify_api'),
    path('login/', TokenObtainPairView.as_view(), name='login_api'),
    path('list/', views.user_list, name='user_list_api')
]