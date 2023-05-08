from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views as jwt_views
from orders.views import OrderView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/orders/", OrderView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
