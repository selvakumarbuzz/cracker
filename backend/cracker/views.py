from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from .serializers import TemplateSerializer,CategorySerializer,ProductSerializer,BillingSerializer,RatingsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404
from api.mixins import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin)
from .models import Template,Category,Product,Billing,Ratings

class TemplateCreate(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content') or None
        # if content is None:
        #     content = title
        serializer.save()
        # send

template_list_create_view = TemplateCreate.as_view()

class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content') or None
        # if content is None:
        #     content = title
        serializer.save()
        # send

category_list_create_view = CategoryCreate.as_view()

class ProductListCreateAPIView(


    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content') or None
        # if content is None:
        #     content = title
        serializer.save()


products_list_create_view = ProductListCreateAPIView.as_view()




class BillingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content') or None
        # if content is None:
        #     content = title
        serializer.save()


billing_list_create_view = BillingListCreateAPIView.as_view()

class RatingsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

    def post(self, request, *args, **kwargs):
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
Ratings_list_create_view = RatingsListCreateAPIView.as_view()
