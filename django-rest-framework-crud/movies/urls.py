from django.urls import path,include
from .views import MovieAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
router = DefaultRouter()
router.register(r'movies',MovieAPIView)
urlpatterns = [
    path('', include(router.urls),),
    path('auth/token',TokenObtainPairView.as_view())
]
