from .models import User
from rest_framework import serializers,status
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail="User with username exists.",code=status.HTTP_403_FORBIDDEN)
        
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with email exists.",code=status.HTTP_403_FORBIDDEN)
        
        phonenumber_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()
        if phonenumber_exists:
            raise serializers.ValidationError(detail="User with phone number exists.",code=status.HTTP_403_FORBIDDEN)
        
        return super().validate(attrs)
        
