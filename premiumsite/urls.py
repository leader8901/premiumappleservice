from django.urls import path, include

from premiumsite.views import index

urlpatterns = [
    path('', index ),
]