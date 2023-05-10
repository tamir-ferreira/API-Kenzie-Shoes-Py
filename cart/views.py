from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from cart.serializers import ProductCartSerializer
from .permissions import IsBuyAccountOwner
from products.models import Product
from .models import Cart
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


class ProductCartView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductCartSerializer
    queryset = Cart.objects.all()

    def perform_create(self, serializer):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))
        quantity = product.stock - self.request.data["quantities"]
        cart = self.queryset.filter(product=product.id).count()
        if cart != 0:
            raise ValidationError({"detail": "Produto já inserido no carrinho"})
        if quantity <= 0:
            raise ValidationError({"detail": "Quantidade de produto indisponível"})
        self.check_object_permissions(self.request, product)
        serializer.save(product=product, user=self.request.user)


class ProductCartDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsBuyAccountOwner]

    serializer_class = ProductCartSerializer
    queryset = Cart.objects.all()
