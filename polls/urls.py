from django.urls import path
from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet

from rest_framework.authtoken import views

from rest_framework.documentation import include_docs_urls

from django.contrib.auth.views import LoginView

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    #path("login/", LoginView.as_view(), name="login"),
    path("login/", views.obtain_auth_token, name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path('swagger-docs/', schema_view),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('docs/', include_docs_urls(title='Polls API')),
]

urlpatterns += router.urls
