from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from rest_framework import permissions
from userapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Youtube",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Xojiakbar Goipov. Email:<xojiakbargoipov3@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReccomendApiView.as_view()),
    path('docs/',schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('videos/', VideoApiView.as_view()),
    path('video/<int:pk>/', VideoApi.as_view()),
    path('efirlar/', EfirApiVIew.as_view()),
    path('efir/<int:pk>/', EfirApi.as_view()),
    path('playlists/', PlaylistApiView.as_view()),
    path('comments/', CommentApiView.as_view()),
    path('comment/<int:pk>', CommentDel.as_view()),
    path('likes/', LikeApiView.as_view()),
    path('kanal/<int:pk>/', KanalApi.as_view()),
    path('users/', Users.as_view()),
    path('user/<int:pk>/', UserGet.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
