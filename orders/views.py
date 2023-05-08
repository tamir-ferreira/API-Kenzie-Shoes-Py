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


class OrderPaginator(PageNumberPagination):
    page_size = 10


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    pagination_class = OrderPaginator

    def perform_create(self, serializer):
        p = User.objects.get(username=self.request.user)
        item_all = p.product.all()
        for item in item_all:
            if item.stock == 0:
                raise ValidationError("Produto indisponível")
            serializer.save(products=item, user=self.request.user)
        send_mail("Testando",
                  "Mensagem via django, ok",
                  settings.EMAIL_HOST_USER,
                  ["andrewairamdasilva@gmail.com"],
                  False)
        
        
class OrderDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAccountOwner]
    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()
