from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from .serializers import RegisterSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message': f'Ползователь({request.data.get('username')}) успешно зарегистрировань!'}, status=201)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': str(user.id),
                'username': user.username,
            }
        }, status=200)

    else:
        return Response({"error": "Неправельный пароль или имя"}, status=401)

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    serializer = TokenRefreshSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as err:
        return Response({"error": str(err)}, status=400)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    token = request.data.get("refresh")
    refresh = RefreshToken(token=token)
    refresh.blacklist()