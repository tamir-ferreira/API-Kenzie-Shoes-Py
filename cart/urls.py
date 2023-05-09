from django.urls import path
from .views import ProductCartDetailView, ProductCartView


urlpatterns = [
    path("cart/<int:pk>/", ProductCartDetailView.as_view()),
]
