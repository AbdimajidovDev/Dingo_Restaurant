from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:pk>/', SingleBlogView.as_view(), name='single-blog'),
]
