from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from user.serializers import UserAccountSerializer
from user.models import UserAccount
from user.permissions import CustomPermission, IsAdminOrSelf

class UserAccountViewSet(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = []  
        elif self.action == "list":
            self.permission_classes = [IsAuthenticated, CustomPermission]
        elif self.action in ["retrieve", "update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsAdminOrSelf]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.is_superuser or request.user == user:
            return super().retrieve(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={"detail": "Forbidden"})

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if not request.user.is_superuser:
            if "is_staff" in request.data or "is_superuser" in request.data:
                raise PermissionDenied("You do not have permission to modify these fields.")
        if request.user.is_superuser or request.user == user:
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={"detail": "Forbidden"})

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user.is_superuser or request.user == user:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={"detail": "Forbidden"})

    @action(detail=False, methods=["GET"])
    def get_user(self, request):
        return Response(UserAccountSerializer(request.user).data)

    @action(detail=False, methods=["GET"])
    def get_user_by_email(self, request):
        email = request.query_params.get("email")
        user = UserAccount.objects.filter(email=email).first()
        if user:
            return Response(UserAccountSerializer(user).data)
        return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "User not found"})

    @action(detail=False, methods=["GET"])
    def get_users_by_role(self, request):
        role = request.query_params.get("role")
        if role:
            users = UserAccount.objects.filter(role=role)
            return Response(UserAccountSerializer(users, many=True).data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Role parameter is required"})

    @action(detail=False, methods=["POST"])
    def update_contact_info(self, request):
        user = request.user
        phone_number = request.data.get("phone_number")
        address = request.data.get("address")

        if phone_number:
            user.phone_number = phone_number
        if address:
            user.address = address
        
        user.save()
        return Response(UserAccountSerializer(user).data)
