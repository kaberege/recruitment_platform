from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Custom user

# Serializer class for user registration
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "role"]

    # Override the creation method to handle user creation logic
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user  # Return the created user

# Serializer class for updating user profile
class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
        
# Serializer class for user login
class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    