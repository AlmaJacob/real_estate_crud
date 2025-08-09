from rest_framework import serializers
from .models import estate, Cart ,User

#CRUD of estate (detail page adding)
class EstateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = estate
        fields = '__all__'
#Listing the estate products
class EstateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = estate
        fields = ['id', 'image', 'title', 'location', 'price']  

# Cart serializer
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'estate']

#registation of user
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user
