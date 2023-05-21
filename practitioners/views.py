from django.shortcuts import render
from rest_framework import generics
from .models import Practitioner
from .serializers import (
    PractitionerSerializer,
    )


class PractitionerListCreateView(generics.ListCreateAPIView):
    queryset = Practitioner.objects.all()
    serializer_class = PractitionerSerializer


class PractitionerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Practitioner.objects.all()
    serializer_class = PractitionerSerializer

