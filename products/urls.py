from django.urls import path
from .views import *
from cart.views import *

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<int:pk>/cart/", ProductCartView.as_view()),
]
