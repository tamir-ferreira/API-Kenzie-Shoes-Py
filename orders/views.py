from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAccountOwner
from rest_framework.pagination import PageNumberPagination
from .serializers import OrderSerializer
from .models import UserOrder
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
from cart.models import Cart


class OrderPaginator(PageNumberPagination):
    page_size = 10


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    pagination_class = OrderPaginator

    def get_queryset(self):
        if not self.request.user.is_staff:
            orders = self.queryset.filter(user=self.request.user.id)
            return orders
        if self.request.user.is_seller:
            product_obj = self.queryset.all().last()
            if self.request.user.id == product_obj.user_id:
                seller_orders = self.queryset.filter(products_id=product_obj.products.id)
                return seller_orders
        return self.queryset

    def perform_create(self, serializer):
        user_obj = User.objects.get(username=self.request.user)
        item_all = user_obj.product.all()
        if item_all.count() == 0:
            raise ValidationError({"detail": "Carrinho está vazio"})
        for item in item_all:
            if item.stock == 0:
                raise ValidationError({"detail": "Produto indisponível"})
            serializer.save(products=item, user=user_obj)
        # send_mail("Testando",
        #           "Mensagem via django, ok",
        #           settings.EMAIL_HOST_USER,
        #           ["andrewairamdasilva@gmail.com"],
        #           False)
        Cart.objects.filter(user_id=user_obj.id).delete()
        
        
class OrderDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

