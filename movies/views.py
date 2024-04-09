from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer    
from .models import MovieData
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import logout
# from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
from django.db.models import signals
from django.dispatch import receiver
from django.conf import settings

@receiver(signals.post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kargs):
    if created:
        Token.objects.create(user=instance)


def logout_user(request):
    logout(request)
    return HttpResponse("user logged out successfully")


class GetAuthToken(APIView):
    
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        if id and Token.objects.filter(user_id=id).exists():
            object = Token.objects.get(user_id=id)
            token = object.key
            return Response({"status":"success","body":f"token {token}"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"failed","boddy":"user doesn't exist"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MovieView(APIView):
    
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        if id:
            if not MovieData.objects.filter(id=id).exists():
                return Response({"status":"failed","body":"Given ID not found"},status=status.HTTP_404_NOT_FOUND)
            object = MovieData.objects.get(id=id)
            serializer = MovieSerializer(instance=object)
            return Response({"status":"success","body":serializer.data},status=status.HTTP_200_OK) 
        else:
            object = MovieData.objects.all()
            serializer = MovieSerializer(instance=object,many=True)
            return Response({"status":"success","body":serializer.data},status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","body":"Data successfully added"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"failed","body":serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request,id=None):#id=None,format=None):
        print("path ",request.path,request.path_info,request.method)
        # id = request.data.get('id',None)
        if id:
            if not MovieData.objects.filter(id=id).exists():
                serializer = MovieSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status":"success","body":"Data successfully added"},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"failed","body":serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            else:
                object = MovieData.objects.get(id=id)
                serializer = MovieSerializer(instance=object,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status":"success","body":"Data Modified Successfully"},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"failed","body":serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response("error",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def patch(self,request,id=None):
        print("path ",request.path,request.path_info,request.method)
        
        object = MovieData.objects.get(id=id)
        serializer = MovieSerializer(instance=object,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","body":"Data modified successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"status":"failed","body":serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self,request,id=None):

        object = MovieData.objects.get(id=id)
        object.delete()
        return Response({"status":"success","body":"Item deleted"},status=status.HTTP_200_OK)
         


# Create your views here.

# class MovieViewSet(viewsets.ModelViewSet):   
#     queryset = MovieData.objects.all()
#     serializer_class = MovieSerializer


# class ActionViewSet(viewsets.ModelViewSet):
#     queryset = MovieData.objects.filter(movie_type='action')
#     serializer_class = MovieSerializer

# @api_view(['GET'])
# def get_movies(request):
    
#     movie_data = MovieData.objects.all()
#     print(movie_data)
#     serializer_data = MovieSerializer(movie_data,many=True)
#     return Response(serializer_data.data)

# @api_view(['POST'])
# def movie_update(request,id):
#     movie = MovieData.objects.get(pk=id)
#     serializer = MovieSerializer(instance=movie,data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
