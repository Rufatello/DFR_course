from rest_framework import serializers
import random
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'surname', 'last_name', 'email', 'password', 'is_active')

    def create(self, validated_data):
        new_code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            surname=validated_data['surname'],
            code=new_code,
            password=validated_data['password']
        )
        user.save()
        return user