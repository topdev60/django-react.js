from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MembersSerializer
from .models import Members
# Create your views here.

class MembersView(viewsets.ModelViewSet):
    serializer_class = MembersSerializer
    queryset = Members.objects.all()