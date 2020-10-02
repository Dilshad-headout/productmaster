from rest_framework import serializers
from .models import Product,BusinessOwner,ListingMember
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','category_name','tgid','product_name']

class ProductMiniSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','category_name']

class ListingMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListingMember
        fields = ['id','name']

class businessSerializers(serializers.ModelSerializer):
    product = ProductSerializers(many=False)
    class Meta:
        model = BusinessOwner
        fields = ['id','business_owner','product']

