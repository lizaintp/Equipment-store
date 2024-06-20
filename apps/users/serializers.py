from rest_framework import serializers
from apps.users import models

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=8, write_only=True)

    class Meta:
        model = models.Users
        fields = ['id', 'username', 'password', 'confirm_password' ]
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Пароли отличаются'})
        return attrs
    
    def create(self, validated_data):
        user = models.Users.objects.create(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user