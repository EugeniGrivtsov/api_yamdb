from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    TitleViewSet,
    CategoryViewSet,
    GenreViewSet,
    ConfirmationCodeView
)

app_name = 'api'


router = SimpleRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router.urls)),
    path("v1/auth/signup/", ConfirmationCodeView.as_view()),
]
