from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

@api_view(['POST','GET'])
def register(request):
    serializer=RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data='Successfully Registered',status=status.HTTP_201_CREATED)









    
    
    