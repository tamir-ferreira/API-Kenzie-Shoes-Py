
from rest_framework.generics import *
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import *
from rest_framework.permissions import *
from .serializers import OrderSerializer
from users.permissions import IsAccountOwner
from products.models import Product


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
     
    # queryset = UserOrder.objects.all()
    # serializer_class = OrderSerializer

    def post(self, request: Request, pk: int) -> Response:
        product = get_object_or_404(Product, id=pk)
        self.check_object_permissions(request, product)
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(products=product, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
