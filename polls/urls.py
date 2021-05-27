from django.urls import include, re_path
from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from .apiviews import PollDetail, PollList, ChoiceList, CreateVote
from .apiviews import PollViewSet

router = DefaultRouter()

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_details'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
]

urlpatterns += router.urls

