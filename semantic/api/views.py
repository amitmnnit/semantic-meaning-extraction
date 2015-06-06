# Create your views here.
from app.models import *
from rest_framework import generics, viewsets, permissions, authentication
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework.views import APIView
from django.core import serializers as object_serializers
import json

def TweetTrend(APIView):
	"""
    Get Trend
    """
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication,)

    def get(self, request, *args, **kw):
    	keywords = Keyword.objects.all()
    	api_status=status.HTTP_200_OK
    	result = obj_str = object_serializers.serialize('json', keywords)
        response = Response(result, status=api_status)
        return response
