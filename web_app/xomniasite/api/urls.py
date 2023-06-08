from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Routing for all the API endpoints using viewsets found in views.py
router.register(r'messages', views.MessageViewSet, "messages")
router.register(r'uniqueships', views.UniqueShipsViewSet, "uniqueships")
router.register(r'avgperhour', views.AverageSpeedViewSet, "avgspeedperhour")
router.register(r'minmaxspeed', views.MinMaxViewSet, "minmaxspeed")
router.register(r'allweather', views.AllWeatherViewSet, "allweather")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
