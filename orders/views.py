from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAccountOwner, IsAdminReadOnly
from rest_framework.pagination import PageNumberPagination
from .serializers import OrderSerializer
from .models import UserOrder
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
from cart.models import Cart
from .permissions import IsSellerUser
from products.models import Product


class OrderPaginator(PageNumberPagination):
    page_size = 10


class OrderView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    pagination_class = OrderPaginator

    def perform_create(self, serializer):
        user_obj = User.objects.get(username=self.request.user)
        item_all = user_obj.user_cart.all()
        if item_all.count() == 0:
            raise ValidationError({"detail": "Carrinho está vazio"})
        for item in item_all:
            product_stock = Product.objects.get(id=item.product_id).stock
            if product_stock <= 0:
                raise ValidationError({"detail": f"{product_stock.name}"})
            quantitie_stock = product_stock - item.quantities
            if quantitie_stock <= 0:
                Product.objects.filter(id=item.product_id).update(stock=0)
            Product.objects.filter(id=item.product_id).update(stock=quantitie_stock)
            serializer.save(products=item.product, user=user_obj)
        order = UserOrder.objects.filter(user_id=self.request.user.id).last()
        msg = f"Prezado(a) {user_obj.first_name}, Gostaríamos de informar que seu ordem de compra foi {order.status}. Agradecemos sua confiança em nossa empresa para suprir suas necessidades e estamos comprometidos em fornecer o melhor serviço possível. Abaixo, você encontrará os detalhes da sua ordem: Número da ordem: {order.id} Data da ordem: {order.buyed_at} Produto: {order.products.name} Valor total: {order.products.value} Nós confirmamos que os produtos solicitados estão disponíveis em nosso estoque e serão enviados o mais breve possível. Caso haja algum problema com a disponibilidade do produto, entraremos em contato para discutir alternativas. Também gostaríamos de lembrar que, caso precise de suporte adicional, nossa equipe está sempre pronta para ajudar. Não hesite em nos contatar por telefone ou e-mail, e estaremos prontos para auxiliá-lo(a) com qualquer dúvida ou necessidade. Mais uma vez, agradecemos por escolher nossa empresa e esperamos continuar atendendo suas necessidades em futuras ocasiões. Atenciosamente, Kenzie Shoes APP"
        send_mail("Confirmação de Ordem de Compra",
                  f"{msg}",
                  settings.EMAIL_HOST_USER,
                  [f"{order.user.email}"],
                  False)
        Cart.objects.filter(user_id=user_obj.id).delete()

        
class OrderDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerUser]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    def perform_update(self, serializer):
        order = self.queryset.get(id=self.kwargs.get("pk"))
        if order.products.user_id != self.request.user.id:
            raise ValidationError({"detail": "You do not have permission to perform this action."})
        serializer.save()
        order = UserOrder.objects.filter(user_id=self.request.user.id).last()
        msg = f"Prezado(a) {order.user.first_name}, Gostaríamos de informar que o status do seu pedido foi alterado para {order.status}. Agradecemos sua confiança em nossa empresa para suprir suas necessidades e estamos comprometidos em fornecer o melhor serviço possível. Atenciosamente, Kenzie Shoes APP"
        send_mail("Alteração do status da ordem de compra",
                  f"{msg}",
                  settings.EMAIL_HOST_USER,
                  [f"andrewairamdasilva@gmail.com"],
                  False)


class BuyOrderView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    pagination_class = OrderPaginator

    def get_queryset(self):
        if not self.request.user.is_staff:
            orders = self.queryset.filter(user=self.request.user.id)
            return orders
        return self.queryset
    

class SellOrderView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerUser]

    serializer_class = OrderSerializer
    queryset = UserOrder.objects.all()

    pagination_class = OrderPaginator

    def get_queryset(self):
        product_obj = self.queryset.all().last()
        if self.request.user.id == product_obj.user_id:
            seller_orders = self.queryset.filter(products_id=product_obj.products.id)
            return seller_orders
        return self.queryset