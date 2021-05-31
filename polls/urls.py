from django.urls import include, re_path
from django.urls.conf import path
from rest_framework.routers import DefaultRouter
from .apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet,basename='polls')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('polls/', PollList.as_view(), name='polls_list'),
    # path('polls/<int:pk>/', PollDetail.as_view(), name='polls_details'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('users/', UserCreate.as_view(), name='user_create')
]

urlpatterns += router.urls

