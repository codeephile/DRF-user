from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import myUser

class myUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = myUser
        fields = ('uuid', 'username', 'email', 'password', 'created_at', 'is_admin', 'is_approved')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = myUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user

class myUserRegisterSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model = myUser
        fields = ('username', 'email', 'password1', 'password2')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Password do not match')
        return data

    def create(self, validated_data):
        user = myUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_id'] = str(user.uuid)
        token['username'] = user.username

        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = myUserSerializer(self.user)
        data.update(serializer.data)
        return data