from django.urls import include, re_path
from django.urls.conf import path
from .views import polls_details, polls_list

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:pk>/', polls_details, name='polls_details')
]