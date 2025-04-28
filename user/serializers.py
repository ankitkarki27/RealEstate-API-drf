from rest_framework import serializers
from user.models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Token serializer to include role and verified status in the JWT token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role  # Add role to the JWT token
        token["verified"] = user.is_verified
        return token


class UserAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for UserAccount model for handling create, update, and delete actions.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "email",
            "password",
            "full_name",  # Use full_name instead of name and last_name
            "phone_number",
            "address",
            "role",  # Include role field
            "is_active",
            "is_verified",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        """
        Custom create method to hash the password before saving the user.
        """
        user = UserAccount.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Update method for handling updates to user fields like full_name, email, and password.
        """
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.address = validated_data.get("address", instance.address)
        instance.role = validated_data.get("role", instance.role)  # Handle role update

        # Only update password if it's provided
        password = validated_data.get("password")
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class UserAccountListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing users with basic details.
    """
    class Meta:
        model = UserAccount
        fields = [
            "id",
            "email",
            "full_name",  # Include full_name in the list view as well
            "role",  # Include role in the list view
            "is_verified",
        ]
