from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAccountOwner
from .serializers import OrderSerializer
from products.models import Product
from .models import UserOrder


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    def perform_create(self, serializer):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))

        if product.stock == 0:
            raise ValidationError("Produto sem estoque.")

        self.check_object_permissions(self.request, product)
        serializer.save(products=product, user=self.request.user)


class OrderDetailView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    def perform_create(self, serializer):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))

        if product.stock == 0:
            raise ValidationError("Produto sem estoque.")

        self.check_object_permissions(self.request, product)
        serializer.save(products=product, user=self.request.user)
