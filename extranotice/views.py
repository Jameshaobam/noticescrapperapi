from django.shortcuts import render,HttpResponse
from .models import ExtraNotice
from scrapper.serializers import ExtraNoticeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ShowNoticesApiView(APIView):
    
 def get(self,request,*args,**kwargs):
    query = ExtraNotice.objects.all().order_by('-date')#latest first

    print(query.all().exists())
    serialiser_query = ExtraNoticeSerializer(query,many=True)
    for i in query:
        print(i)
    print(serialiser_query.data)
    if query.all().exists():
      return Response({
          'status':'Working',
          'data':serialiser_query.data,
        },
        status=status.HTTP_200_OK)
    return Response({
        'status':'No notice available', 
    },status=status.HTTP_200_OK)

def post(self, request, *args, **kwargs):
    return Response({
'status':'Post request service not avialable for now'
    }, status=status.HTTP_404_NOT_FOUND)

