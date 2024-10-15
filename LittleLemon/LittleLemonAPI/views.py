from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all() # Retrieve all records
    serializer_class = MenuItemSerializer # To display and store the record