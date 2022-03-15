from rest_framework import serializers 
from .models import *

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =['owner','phone','country_code','first_name', 'last_name' , 'is_fav']