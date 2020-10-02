from .models import Product,ListingMember
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import ProductSerializers,ProductMiniSerializers,ListingMemberSerializers,UserSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


#### views from html template
def first(request):
    product = Product.objects.all()
    return render(request,'first_temp.html',{'books':product})

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductMiniSerializers
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,) -- use to restrict only for this viewsets with allowany in settings

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductSerializers(instance)
        return Response(serializer.data)

class listingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingMemberSerializers
    queryset = ListingMember.objects.all()
    authentication_classes = (TokenAuthentication,)

    #action takes when something is posted
    @action(detail=True, methods=['POST'])
    def list_done(self,request,pk=None):
        if 'name' in request.data:
            member = ListingMember.objects.get(id=pk)
            print(request.user)
            name = request.data['name']
            user = request.user
            response = {'message': 'its working'}
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {'message': 'Please provide name'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
