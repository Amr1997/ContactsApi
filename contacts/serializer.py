from rest_framework import serializers 
from .models import *

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Contact
        fields =['owner','phone','country_code','first_name', 'last_name' , 'is_fav']