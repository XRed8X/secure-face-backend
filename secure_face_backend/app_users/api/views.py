from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from app_users.models import CustomUser
from app_users.api.serializers import CustomUserSerializer, CreateCustomUserSerializer, LoginSerializer
from rest_framework.authentication import TokenAuthentication


class RegisterUserView(generics.CreateAPIView):
    """ Vista para registrar un nuevo usuario """
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer
    permission_classes = [AllowAny]  # Permite el acceso sin autenticación

    def post(self, request, *args, **kwargs):
        """ Método POST para registrar el usuario """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Crea el usuario con la contraseña hasheada
            token, created = Token.objects.get_or_create(user=user)  # Crea o obtiene el token
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserListCreateView(generics.ListCreateAPIView):
    """ Listar todos los usuarios y crear un nuevo usuario """
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCustomUserSerializer
        return CustomUserSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ Recuperar, actualizar y eliminar un usuario por ID """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class LoginView(APIView):
    """ Vista para manejar el inicio de sesión """
    permission_classes = [AllowAny]  # Permite el acceso a cualquier usuario

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)  # Crea o obtiene el token
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
