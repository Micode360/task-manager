from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        
        validate_password(data['password'])
        return data
    

    def create(self, validated_data):
        try:
            user = User(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                role=validated_data['role']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})
        