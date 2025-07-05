from django.shortcuts import render
from rest_framework import generics
from .models import Enquiry
from .serializers import EnquirySerializer

class getEnquiry(generics.ListCreateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

class getEnquiryById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    lookup_field = 'pk'

