from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.tasks import verifications
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()
        verifications.delay(user.id)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def activate(self, request, *args, **kwargs):
        id = request.data.get('id')
        code = request.data.get('code')

        user = User.objects.get(pk=id)
        if user.code == code:
            user.is_active = True
            user.save()

        return Response({'message': 'Пользователь активирован'}, status=status.HTTP_200_OK)




