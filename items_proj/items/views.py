from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Item
from .serializers import ItemSerializer

class ItemPagination(PageNumberPagination):
    page_size = 10  

class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    pagination_class = ItemPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        return Item.objects.order_by('id')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = Item(**serializer.validated_data)
        item.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            return Response({'error': exc.detail}, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer

    def get_object(self):
        obj_id = self.kwargs.get("pk")
        return get_object_or_404(Item, id=obj_id)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
