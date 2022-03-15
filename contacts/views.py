
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import *
from .serializer import *
# Create your views here.

class ContactsViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    permission_classes=(permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    