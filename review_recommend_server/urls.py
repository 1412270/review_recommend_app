from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('movies', views.MoviesViewSet, 'movies')
router.register('movie', views.MovieDetailViewSet, 'movie')
router.register('users', views.UserViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # if you want authenticated with oauth2
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
