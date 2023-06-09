from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.exceptions import TokenError
from .models import CustomUser, AccessTokenOutStand
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import RegisterSerialzier, LoginSerializer, ObtainTokenSerializer
from django.core.cache import cache


class AuthViewSet(viewsets.ViewSet):
    def get_token_response(self, request, user):
        login(request, user)
        refresh = RefreshToken.for_user(user)

        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        AccessTokenOutStand.objects.create(
            refresh_token=refresh_token,
            access_token=access_token
        )

        return Response(
            status=status.HTTP_200_OK, data=ObtainTokenSerializer({
                'refresh_token': refresh_token,
                'access_token': access_token
            }).data
        )


class Register(AuthViewSet):
    serializer_class = RegisterSerialzier

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return self.get_token_response(request, user)


class LogIn(AuthViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            user = CustomUser.objects.filter(username=data["username"]).first()

            if user and user.check_password(data["password"]):
                return self.get_token_response(request, user)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN, data={"Message": "The information is invalid."})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class LogOut(viewsets.ViewSet):
    """
    Logged out user.
    """

    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        Receives a valid refresh token and sets that into the blacklist to log out the user.
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            access_token_obj = AccessTokenOutStand.objects.filter(access_token=request.access_token).first()
            access_token_obj.is_valid = False
            access_token_obj.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'Bad token': 'Token is expired or invalid.'})


class VerifyToken(viewsets.ViewSet):

    def create(self, request):
        token = request.data.get('token', None)

        if not token:
            return Response(data={'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        user_id = cache.get(token)
        if user_id is not None:
            # If the user ID is in the cache, return it
            print('from cache')
            return Response(data={'user_id': user_id}, status=status.HTTP_200_OK)

        try:
            decoded_token = AccessToken(token, verify=True).payload
        except TokenError as err:
            return Response(
                data={'error': str(err)},
                status=status.HTTP_400_BAD_REQUEST
            )

        if decoded_token:
            user_id = decoded_token.get('user_id')

            # Cache the user ID for future requests
            expiration_time = decoded_token.get('exp') - decoded_token.get('iat')
            cache_success = cache.set(token, user_id, timeout=expiration_time)

            if not cache_success:
                print('Cache set failed')

            return Response(data={'user_id': user_id}, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
