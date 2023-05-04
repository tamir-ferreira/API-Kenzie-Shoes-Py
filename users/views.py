from rest_framework.generics import *
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import *


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
