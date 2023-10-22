from rest_framework import serializers

from contacts.models import Contact



class ContactSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model=Contact
        fields=['id','first_name','last_name','phone_number']
    id=serializers.ReadOnlyField()
        
        
        
class UpdateContactSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)
    phone_number=serializers.CharField(required=False)
    class Meta:
        model=Contact
        fields=['first_name','last_name','phone_number']
        
        
        
    def update(self,instance,validated_data):
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.phone_number=validated_data.get('phone_number',instance.phone_number)
        instance.save()
        return instance
    
    