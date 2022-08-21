from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from rest_framework import permissions
from userapp.views import *
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
    path('', Posts.as_view()),
    path('docs/',schema_view.with_ui('swagger', cache_timeout=0), name='swagger-doc'),
    path('post/<int:pk>/', PostView.as_view()),
    path('users/', Users.as_view()),
    path('user/<int:pk>/', UserGet.as_view()),
    path('efirlar/', Efirlar.as_view()),
    path('efir/<int:pk>/', EfirGet.as_view()),
    path('medias/', Medias.as_view()),
    path('media/<int:pk>/', MediaGet.as_view()),
    path('profils/', Profils.as_view()),
    path('profil/<int:pk>/', ProfilGet.as_view()),
    path('connections/', Connections.as_view()),
    path('connection/', ConnectionDelete.as_view()),

]
