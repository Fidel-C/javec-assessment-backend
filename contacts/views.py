from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from contacts.models import Contact
from contacts.serializers import ContactSerialiser

# Create your views here.




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_contactS(request):
    contacts=request.user.contact_set.all()
    serializer=ContactSerialiser(contacts,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])    
def post_contact(request):
    serializer=ContactSerialiser(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(user=request.user)
    return Response(data=serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET'])
def get_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    serializer=ContactSerialiser(contact)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    serializer=ContactSerialiser(contact,data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)




api_view(['DELETE'])
def delete_contact(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    serializer=ContactSerialiser(data=contact)
    return Response(data=serializer.data,status=status.HTTP_204_NO_CONTENT)
    
    
    