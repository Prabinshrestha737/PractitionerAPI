from django.urls import path
from practitioners.views import (
    PractitionerListCreateView,
    PractitionerRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('practitioners/', PractitionerListCreateView.as_view(), name='practitioner-list'),
    path('practitioners/<int:pk>/', PractitionerRetrieveUpdateDestroyView.as_view(), name='practitioner-detail')
]