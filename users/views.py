from rest_framework.generics import *
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from addresses.models import Address
from .permissions import *
from rest_framework.permissions import *


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer