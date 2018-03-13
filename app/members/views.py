from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Member
from .serializers import MemberSerializer

# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated, )

class MemberList(APIView):

    def get( self, request ):
        member_list = Member.objects.all()
        serializer = MemberSerializer(member_list, many=True)
        return Response(serializer.data)