from . import views
from django.urls import path
urlpatterns=[
    path('enquiry/',views.getEnquiry.as_view()),
    path('enquiry/<int:pk>/',views.getEnquiryById.as_view())
]