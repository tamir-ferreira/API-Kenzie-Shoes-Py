from cart.serializers import *
from .models import *
from rest_framework.generics import *
from users.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import *


class ProductCartView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    # queryset = ProductCart.objects.all()
    # serializer_class = ProductCartSerializer

    def post(self, request: Request, pk: int) -> Response:

        product = get_object_or_404(Product, id=pk)
        self.check_object_permissions(request, product)
        serializer = ProductCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product, cart=request.user.cart)

        return Response(serializer.data, status.HTTP_201_CREATED)

    # def perform_create(self, serializer):
    #     product_id = self.kwargs['pk']
    #     print(product_id)
        # serializer.save(cart=self.request.user.cart, product=product_id)
        # product = get_object_or_404(Product, self.request.)
        # serializer.save(user=self.request.user)