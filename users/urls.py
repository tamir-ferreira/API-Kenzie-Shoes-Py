from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from orders.views import OrderView

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
    path("users/<int:pk>/orders/", OrderView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
